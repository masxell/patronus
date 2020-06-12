from django.contrib import admin
from .models import Reference

# Register your models here.
#admin.site.register(Reference)
@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'author', 'created', 'updated', 'publish')
    list_filter = ('created', 'author', 'publish')
    search_fields = ('title',)
    #prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('title', 'author', 'publish')