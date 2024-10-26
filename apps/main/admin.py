from django.contrib import admin
from apps.main.models import Main,Artist,Event,Blog
# Register your models here.

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'logo', 'facebook', 'instagram', 'youtube']
    
@admin.register(Artist)
class MainAdmin(admin.ModelAdmin):
    fields = ['name','location','description','photo']
    
@admin.register(Event)
class MainAdmin(admin.ModelAdmin):
    fields = ['title','description','image','date']

    
@admin.register(Blog)
class MainAdmin(admin.ModelAdmin):
    fields = ['image','title','description']
    