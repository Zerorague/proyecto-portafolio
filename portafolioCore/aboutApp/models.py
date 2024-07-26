from django.db import models

# Create your models here.
class Formacion(models.Model):
    carrera = models.CharField(max_length=255)
    institucion = models.CharField(max_length=255,default="")
    ingreso= models.DateField()
    egreso = models.DateField(null= True, blank= True)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'
        ordering = ["-ingreso",]
    def __str__(self) -> str:
        return self.carrera

class Trabajo(models.Model):
    titulo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    ingreso= models.DateField()
    egreso = models.DateField(null= True, blank= True)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'trabajo'
        verbose_name_plural = 'trabajos'
        ordering = ["-ingreso",]

    def __str__(self) -> str:
        return self.empresa
    
class Nivel(models.Model):
    nivel = models.CharField(max_length=50,unique=True)
    def __str__(self) -> str:
        return self.nivel
    

class Habilidad(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.ForeignKey(Nivel,null=True,on_delete=models.SET_NULL)
    imagen = models.ImageField(upload_to="habilidades")
    class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'habilidades'
        ordering = ["nombre",]
    
    
    def __str__(self) -> str:
        return self.nombre



