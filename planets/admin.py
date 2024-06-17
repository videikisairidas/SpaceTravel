from django.contrib import admin
from planets.models import Planets, Objects

# Register your models here.
class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'planet_name')

    def planet_name(self, obj):
        return obj.planetID.name
    planet_name.short_description = 'Planet Name'

admin.site.register(Planets)
admin.site.register(Objects, ObjectsAdmin)

