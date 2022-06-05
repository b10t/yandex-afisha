from django.contrib import admin

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


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
