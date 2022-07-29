from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms



# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')


class LinksCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_published',)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'user', 'email', 'created')
    list_display_links = ('id', 'title', 'user', 'email')
    search_fields = ('name', 'title', 'content', 'email', 'user')
    list_filter = ('user', 'name', 'title', 'email')


class ScriptCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ScriptsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    additional = forms.CharField(widget=CKEditorUploadingWidget())
    code = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Scripts
        fields = '__all__'


class ScriptsAmin(admin.ModelAdmin):
    form = ScriptsAdminForm
    list_display = ('id', 'title', 'category', 'created', 'updated', 'is_published')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title', 'description', 'code', 'additional', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'description', 'code', 'additional', 'is_published', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    save_on_top = True


admin.site.register(Links, LinksAdmin)
admin.site.register(LinksCategory, LinksCategoryAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(ScriptCategory, ScriptCategoryAdmin)
admin.site.register(Scripts, ScriptsAmin)
admin.site.site_title = 'Управление NS_GaT'
admin.site.site_header = 'УПРАВЛЕНИЕ'
