from django.db import models
from applications.department.models import Department

# Create your models here.

class Skills(models.Model):
    skill = models.CharField('Skill', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades de empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.skill

class Employe(models.Model):
    """ Modelo para tabla de empleados """
    
    jobs = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    
    first_name = models.CharField('Name', max_length = 50)
    last_name  = models.CharField('Last name', max_length = 50)
    # Enum para valores como Contador - Administrador - Economista - Otro
    job = models.CharField('job', max_length = 50, choices = jobs)
    departmen = models.ForeignKey(Department, on_delete = models.CASCADE)
    image = models.ImageField('image', upload_to = 'static', height_field = None, width_field = None, max_length = None, null = True)
    skills = models.ManyToManyField(Skills)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-first_name']
        unique_together = ('first_name', 'last_name')
        
    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name
