from django.contrib import admin
from mainapp.models import Equipments, Records

# Register your models here.
class EquipmentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'equip_attribute', 'equip_status', 'author', 'equip_storagespace', 'registered_date',)
	list_display_links = ('id', 'name',)

class RecordsAdmin(admin.ModelAdmin):
	list_display = ('id', 'equipid', 'userid', 'status', 'recorded_date', 'return_due', 'returned_date',)
	list_display_links = ('id',)

admin.site.register(Equipments, EquipmentsAdmin)
admin.site.register(Records, RecordsAdmin)
