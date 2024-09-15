from django.db import models

# Create your models here.

class  Department(models.Model):
    name = models.CharField('Name', max_length = 50, unique=True)
    short_name = models.CharField('Short name', max_length = 20, null=True, unique=True)
    anulate = models.BooleanField('Anulate', default = False)
    
    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'short_name')
    
    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.short_name
    