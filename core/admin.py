from django.contrib import admin

# Register your models here.
from core.models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Country)
