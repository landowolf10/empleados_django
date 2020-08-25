from django.db import models
from applications.departamento.models import DepartamentoModel

# Create your models here.
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

    def __str__(self):
        return self.first_name + ' ' + self.last_name + '-' + str(self.job)