from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(verbose_name="titulo",null=False,max_length=35)
    description = models.TextField(verbose_name="descripcion")
    image = models.ImageField(verbose_name="imagen",upload_to="proyectos")
    link = models.URLField(verbose_name="enlace",max_length=180,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created",]
    def __str__(self) -> str:
        return self.title
