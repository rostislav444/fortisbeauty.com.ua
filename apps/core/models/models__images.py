from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from project import settings
from unidecode import unidecode
import os, io, json, PIL


def middle_color(filename):
    #Resizing parameters
    width, height = 1,1
    try:
        image = PIL.Image.open(filename)
        image = image.resize((width, height),resample = 0)
        #Get colors from image object
        pixels = image.getcolors(width * height)
        x = pixels[0][1]
        return '#{:02x}{:02x}{:02x}'.format(x[0],x[1],x[2])
    except:
        return '#ffffff'
   



class ModelImages(models.Model):
    id = models.AutoField(primary_key=True)

    IMAGES_SIZES = {
        'l':2400, 
        'm':1200, 
        's':480, 
        'xs':80
    }

    class Meta:
        abstract = True

    def dir_path(self):
        path = ""
        root = settings.MEDIA_ROOT
        for level in [self._meta.app_label, self._meta.model_name]:
            path += level + '/'
            if not os.path.isdir(root + path): 
                os.mkdir(root + path)
        return path
    
    def human_name(self, field_name):
        inst = self
        instances = [inst]
        if hasattr(inst,'parent'):
            instances.append(inst.parent)
        elif hasattr(inst,'product'):
            instances.append(inst.product)
       
        name_parts = [field_name]
        
        for inst in instances:
            if hasattr(inst, 'make_slug'):
                name_parts.append(inst.make_slug)
                break
            for attr in ['slug','name','title','code','category','create']:
               
                if hasattr(inst, attr):
                    attr = getattr(inst, attr)
                    if attr is not None:
                        name_parts.append(slugify(unidecode(str(attr))))
                        break
        if not self.id:
            last_obj = type(self).objects.order_by('pk').last()
            if last_obj: id = last_obj.pk + 1
            else: id = 1
        else:
            id = self.id
       
        return '-'.join(name_parts)[:50] + '-id-'+str(id)

    def ext_convert(self, ext):
        if ext == 'png': 
            return "RGBA","PNG"
        else: 
            return "RGB","JPEG"   

    def get_image_io(self, file, ext):
        if ext in ['gif','mp4']:
            image_io = io.BytesIO(file.read())
            image_io.seek(0)
            return image_io
        else:
            image_io = io.BytesIO()
            img_convert, img_format = self.ext_convert(ext)
            image = PIL.Image.open(file).convert(img_convert)
            image.save(image_io, format=img_format)
            image.close()
            return image_io
        return None

    def img_size_path(self, key, path, ext):
        if key == 'l': 
            return path+'.'+ext
        else:           
            return path+'_'+key+'.'+ext

    def make_thumbs(self, field_name, image_io, ext):
        thmbs = {}           
        base_path = self.dir_path() + self.human_name(field_name)
        prev_w, prev_h = (0,0)
        prev_path = None

        if ext in ['jpg','jpeg','png']:
            for key, size in self.IMAGES_SIZES.items():
                path = self.img_size_path(key, base_path , ext)
                image = PIL.Image.open(image_io)
                w, h = image.size
                if key == 'l':
                    setattr(getattr(self, field_name), 'name', path)
                img_convert, img_format = self.ext_convert(ext)
                image = image.convert(img_convert)
                if key == 'l' or size <= prev_w:
                    image.thumbnail((size, size), PIL.Image.ANTIALIAS)
                    image.save(settings.MEDIA_ROOT + path, img_format)
                    w, h = image.size
                else:
                    path = prev_path
                    w,h = (prev_w, prev_h)

                thmbs[key] = {
                    'url':path, 'path': settings.MEDIA_URL + path,
                    'w':w, 'h':h, 'ext':ext
                }
                prev_w, prev_h = (w,h)
                prev_path = path
        elif ext == 'gif':
            main_path = f'{base_path}.{ext}'
            path = settings.MEDIA_ROOT + main_path
            default_storage.save(path, image_io)
            setattr(getattr(self, field_name), 'name', main_path)
            for key, size in self.IMAGES_SIZES.items():
                thmbs[key] = {
                    'url':path, 'path': settings.MEDIA_URL + main_path,
                    'w':400, 'h':400, 'ext':ext
                }
                
        return thmbs

    def get_thmbs(self, field):
        thmbs_name =  field.name + '_thmb'
        thmbs = getattr(self, thmbs_name)
        if type(thmbs) == str:
            thmbs = json.dumps(json.loads(thmbs.replace("'",'"')), indent=4)
        return thmbs, thmbs_name

    
    def get_old_image(self, thmbs):
        try:    
            old_image = thmbs['l']['url']
        except: 
            old_image = None
        return old_image

    

    def save(self):
        for field in self._meta.get_fields():
            if field.get_internal_type() == 'FileField':
                image_field = getattr(self, field.name)
               
                try: 
                    file = image_field.file
                except:  continue
            
                thmbs, thmbs_name = self.get_thmbs(field)
                old_image = self.get_old_image(thmbs)

                if image_field.name is not None and image_field.name != old_image:
                    ext = image_field.name.split('.')[-1].lower()

                    image_io = self.get_image_io(file, ext)
                    self.delete_old()
                    image_field.delete(save=False)
                    super(ModelImages, self).save()
                    thmbs = self.make_thumbs(field.name, image_io, ext)
                    setattr(self, thmbs_name, thmbs)
       
        super(ModelImages, self).save()

    def clean(self):
        for field in self._meta.get_fields():
            if field.get_internal_type() == 'FileField':
                filename = getattr(self, field.name).name
                if filename:
                    ext = filename.split('.')[-1]
                    if ext not in ['jpg', 'jpeg', 'webp', 'png', 'gif', 'mp4']:
                        raise ValidationError({field.name : f'Файл формата ."{ext}" не допустим для этого поля',})


    def delete_old(self):
        for field in self._meta.get_fields():
            if field.get_internal_type() == 'FileField':
                image_field = getattr(self, field.name)
                thmbs_name =  field.name + '_thmb'
                thmbs =       getattr(self, thmbs_name)
                if thmbs:
                    for image in thmbs.values():
                        if type(image) == dict:
                            path = settings.MEDIA_ROOT + image['url']
                            try:os.remove(path)
                            except: pass
        return {}



    def delete(self):
        self.delete_old()
        super(ModelImages, self).delete()



class Images(ModelImages):
    num =        models.PositiveIntegerField(default=0, verbose_name="№")
    image =      models.FileField(max_length=1024, null=True, blank=True, verbose_name=_("Изображение"))
    image_thmb = models.JSONField(editable=True, null=True, blank=True, default=dict)

    class Meta:
        abstract = True


   


