from __future__ import unicode_literals
from django.contrib import admin
from django.core import urlresolvers
from django.utils.html import format_html
from museum.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'first_name', 'last_name', 'pseudonym', 'date_of_birth', 'date_of_death')
    search_fields = ('first_name', 'last_name', 'pseudonym', 'date_of_birth', 'date_of_death')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'pseudonym', 'date_of_birth', 'date_of_death')
        }),
    )


admin.site.register(Author, AuthorAdmin)


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('label', 'usage', 'url')
    fieldsets = (
        (None, {
            'fields': ('label', 'usage', 'url')
        }),
    )


admin.site.register(License, LicenseAdmin)

'''
class SourceAdmin(admin.ModelAdmin):
    list_display = ('copyright_notice', 'source')
    search_fields = ('copyright_notice', 'source')
    fieldsets = (
        (None, {
            'fields': ('copyright_notice', 'source')
        }),
    )

admin.site.register(Source, SourceAdmin)
'''


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    search_fields = ('title', 'url',)
    fieldsets = (
        (None, {
            'fields': ('title', 'url',)
        }),
    )


admin.site.register(Link, LinkAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = (
    'title', 'subtitle', 'year', 'uuid', 'madek', 'show_image')  # 'show_image', 'link_to_author', 'source'
    list_filter = ('author', 'year', 'tags', 'license',)
    search_fields = (
    'image', 'title', 'description', 'year', 'author__first_name', 'author__last_name', 'author__pseudonym')
    readonly_fields = ('uuid', 'created', 'modified', 'title', 'subtitle', 'year', 'source',
                       'copyright_notice', 'author', 'license')

    # prepopulated_fields = {'slug': ('title',)}

    # change_form_template = 'museum/admin/change_form.html'

    def madek(self, obj):
        if obj.remote_uuid is not None:
            return format_html(
                '<a href="http://medienarchiv.zhdk.ch/entries/{}">{}</a>',
                obj.remote_uuid,
                obj.remote_uuid
            )

    madek.short_description = 'MAdeK'

    def show_image(self, obj):
        if obj.image:
            return format_html(
                '<img src={} width=100px />',
                obj.image.url
            )
        else:
            return ''

    show_image.short_description = 'Image'

    '''
    def link_to_author(self, obj):
        if obj.author is not None:
            url = urlresolvers.reverse("admin:museum_author_change", args=[obj.author.id])
            return format_html(
                '<a href="{}">{}</a>',
                url,
                obj.author.get_full_name()
            )
    link_to_author.short_description = 'Author'
    '''

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'uploader':
            kwargs['initial'] = request.user.id
        return super(EntryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': (
            'image', 'author', 'year', 'title', 'subtitle', 'description', 'tags', 'source', 'copyright_notice', 'license',
            'link')
        }),

        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('uploader',)
        }),

    )


admin.site.register(Entry, EntryAdmin)
