from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Genre)
