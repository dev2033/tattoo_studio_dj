from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm

from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class WorkMasterAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display_links = ('name', 'id', 'master_name')
    list_display = ('id', 'name', 'master_name')
    prepopulated_fields = {'slug': ('name',)}


class StudioAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

    save_on_top = True
    list_display = ('id', 'title', 'slug', 'created_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('tags',)
    readonly_fields = ('views', 'created_at', 'get_image')
    fields = ('title', 'slug', 'tags', 'master',
              'content', 'image', 'get_image',
              'views', 'created_at')

    def get_image(self, obj):
        """Возвращает картинку новости в админке"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return '-'

    get_image.short_description = 'Фото'


class MasterAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = \
            mark_safe(
                """
                <span style="color:red; font-size:14px;">
                    Рекомендуемый размер изображения: Ширина - 810 пикселов | 
                    Высота 1080 пикселов
                </span>
                """)


class MasterAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'positions', 'get_image')
    list_display_links = ('name', 'get_image')
    form = MasterAdminForm

    def get_image(self, obj):
        """Возвращает фото мастера"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return '-'

    get_image.short_description = 'Фото'

    class Meta:
        model = Master
        fields = '__all__'


admin.site.register(Master, MasterAdmin)
admin.site.register(WorkMaster, WorkMasterAdmin)
admin.site.register(TattooCategory)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AboutStudio, StudioAdmin)


admin.site.site_title = 'Административная панель сайта Тату-студии "Якорь"'
admin.site.site_header = 'Административная панель сайта Тату-студии "Якорь"'
