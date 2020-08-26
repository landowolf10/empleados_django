from django.db import models
from applications.departamento.models import DepartamentoModel
from ckeditor.fields import RichTextField

class HabilidadesModel(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habiidades empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class EmpleadoModel(models.Model):
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(DepartamentoModel, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(HabilidadesModel)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Modelo Empleado de prueba'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + '-' + str(self.job)