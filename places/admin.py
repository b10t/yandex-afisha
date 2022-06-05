from django.contrib import admin
from django.utils.html import mark_safe

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'preview_image', 'position', )

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return mark_safe(
            '<img src="{url}" height={height} />'.format(
                url=obj.image.url,
                height=200,
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


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('position', 'place', )
    list_display_links = ('place', )
    search_fields = ('place', )

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return mark_safe(
            '<img src="{url}" height={height} />'.format(
                url=obj.image.url,
                height=200,
            )
        )
