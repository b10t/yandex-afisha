from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html, mark_safe

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'preview_image', 'position', )

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return format_html(
            '{}',
            mark_safe(
                '<img src="{url}" height={height} />'.format(
                    url=obj.image.url,
                    height=200,
                )
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )

    inlines = [
        PlaceImageInline,
    ]
