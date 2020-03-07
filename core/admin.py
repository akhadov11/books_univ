from django.contrib import admin

from core.models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
        class for representing Genres in admin panel
    """
    list_display = ("id", "name")
    list_editable = ("name",)
    search_fields = ("id", "name")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
        class for representing Countries in admin panel
    """
    list_display = ("id", "name",)
    list_editable = ("name",)
    search_fields = ("id", "name")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
        class for representing Cities in admin panel
    """
    list_display = ("id", "name", "country")
    list_editable = ("name",)
    search_fields = ("id", "name")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
        class for representing Authors in admin panel
    """
    list_display = ("id", "name", "city")
    list_display_links = ("name",)
    search_fields = ("name",)
    ordering = ("id", "name")


class PriceListFilter(admin.SimpleListFilter):
    """
        filtering books by price
    """
    title = "price range"
    parameter_name = "price"

    def lookups(self, request, model_admin):
        return (
            ('low', 'Low priced books'),
            ('norm', 'Normally priced books'),
            ('exp', 'Expensive books'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__gte=0, price__lte=50)
        if self.value() == 'norm':
            return queryset.filter(price__gte=51, price__lte=250)
        if self.value() == 'exp':
            return queryset.filter(price__gte=151)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
        class for representing Books in admin panel
    """
    list_display = ("id", "name", "price", "pub_date", "author")
    list_filter = (PriceListFilter, "pub_date")
    list_editable = ("name",)
    readonly_fields = ("pub_date",)
    raw_id_fields = ("author",)
    ordering = ("id",)
    search_fields = ("name", "price")
    date_hierarchy = "pub_date"

