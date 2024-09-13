from django.contrib import admin
from .models import News, Construction, Subsidy, Tag
from django.contrib.admin.sites import AdminSite
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

#管理名変更
AdminSite.site_header = 'Cozy design'
AdminSite.site_title = 'サイト管理者'
AdminSite.index_title = '管理画面'


#お知らせ
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'pub_date')

    def thumbnail_preview(self, obj):
        if hasattr(obj, 'thumbnail') and obj.thumbnail:
           return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))
        else:
           return '(No thumbnail)'

    thumbnail_preview.short_description = 'サムネイル'

admin.site.register(News, NewsAdmin)



#施工事例
class ConstructionAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    fieldsets = (
        (None, {
            'fields': (('title',), ('slug',), ('image',),
                      ('kitchen_B', 'kitchen_A'), ('toilet_B', 'toilet_A'),
                      ('living_B', 'living_A'), ('entrance_B', 'entrance_A'),
                      ('stairs_B', 'stairs_A'), ('etc_B', 'etc_A'), 'body')
        }),
    )

admin.site.register(Construction, ConstructionAdmin)



#補助金
class SubsidyAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

class SubsidyAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'pub_date')

    def thumbnail_preview(self, obj):
        if hasattr(obj, 'thumbnail') and obj.thumbnail:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))
        else:
            return '(No thumbnail)'

    thumbnail_preview.short_description = 'サムネイル'

admin.site.register(Subsidy, SubsidyAdmin)