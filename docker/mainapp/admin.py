from django.contrib import admin
from mainapp.models import Equipments

# Register your models here.
class EquipmentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'equip_attribute', 'equip_status', 'registered_date',)
	list_display_links = ('id', 'name',)

admin.site.register(Equipments, EquipmentsAdmin)

