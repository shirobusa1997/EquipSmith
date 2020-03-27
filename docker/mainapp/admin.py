from django.contrib import admin
from mainapp.models import Equipments, Records

# Register your models here.
class EquipmentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'equip_attribute', 'equip_status', 'registered_date',)
	list_display_links = ('id', 'name',)

class RecordsAdmin(admin.ModelAdmin):
	list_display = ('id', 'equipid', 'recorded_date',)
	list_display_links = ('id',)

admin.site.register(Equipments, EquipmentsAdmin)
admin.site.register(Records, RecordsAdmin)
