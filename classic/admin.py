from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    #sluglarni avto yozadi
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

class BlockAdmin(admin.ModelAdmin):
    #sluglarni avto yozadi
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    # admin paneldagi blocklarning holati
    list_display = ('title', 'slug', 'created_at', 'get_photo')
    #admin panel blocklarni link holatiga keltiradi
    list_display_links = ('title', 'slug', 'created_at', 'get_photo')
    #admin panel qidiruv satri
    search_fields = ('title',)
    #admin panel saralash 
    list_filter = ('title',)

    def get_photo(self, obj):
        if obj.view:
            return mark_safe(f'<img src="{obj.view.url}" width="50">')

        else:
            return "--"


admin.site.register(Block, BlockAdmin)
admin.site.register(Category, CategoryAdmin)