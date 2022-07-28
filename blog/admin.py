from django.contrib import admin
from .models import *

# Register your models here.


class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')


class LinksCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'user', 'email')
    list_display_links = ('id', 'title', 'user', 'email')
    search_fields = ('name', 'title', 'content', 'email', 'user')
    list_filter = ('user', 'name', 'title', 'email')


admin.site.register(Links, LinksAdmin)
admin.site.register(LinksCategory, LinksCategoryAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
