from django.db import models

# Create your models here.
class  Department(models.Model):
    name = models.CharField('Name', max_length = 50)
    short_name = models.CharField('Short name', max_length = 20)
    anulate = models.BooleanField('Anulate', default = False)
    
    def __str__(self):
        return self.id + '-' + self.titulo + '-' + self.short_name