from django.contrib import admin
from .models import Employe, Skills
# Register your models here.
admin.site.register(Skills)

class AdminEmploye(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departmen',
        'job',
        'full_name'
    )
    
    def full_name(self, obj):
        full_name = obj.first_name + ' ' + obj.last_name
        return full_name
    
    search_fields = (
        'id',
        'first_name',
        'last_name',
        'job'
        )
    
    list_filter = (
        'departmen',
        'job',
        'skills'
    )
    filter_horizontal = ('skills',)
    
admin.site.register(Employe, AdminEmploye)
