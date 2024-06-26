from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from visualizador_cc.users.models import User

class ModeloBase(models.Model):
    id: models.AutoField(primary_key= True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoria', max_length = 100, unique=True)
    

        
    def __str__(self):
        return self.nombre
    
class Noticia (ModeloBase):
    titulo = models.CharField('Titulo del Post', max_length=150, unique=True)
    descripcion = models.TextField('Descripcion', max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextUploadingField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'static/images', max_length=255)
    fecha_publicacion = models.DateField('Fecha de Publicacion', auto_now = False, auto_now_add=True, blank=True)
    

    def __str__(self):
        return self.titulo
    
    class Meta ():
        ordering = ["fecha_publicacion"]