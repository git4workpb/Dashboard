from django.contrib import admin
from .models import ProductMaster, MachineMaster, JobCard, PartyMaster, PartyAddress, BOM, BOMItems

@admin.register(ProductMaster)
class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('product_item_name', 'category', 'unit', 'opening_stock', 'rate')
    search_fields = ('product_item_name', 'category')

@admin.register(MachineMaster)
class MachineMasterAdmin(admin.ModelAdmin):
    list_display = ('name_of_machine', 'machine_process_name', 'mould', 'machine_capacity', 'machine_final_produce_product_name')
    search_fields = ('name_of_machine', 'machine_process_name')

@admin.register(JobCard)
class JobCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'machine_name', 'product_name', 'product_qty')
    search_fields = ('machine_name__name_of_machine', 'product_name__product_item_name')

@admin.register(PartyMaster)
class PartyMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'party_name')
    search_fields = ('party_name',)

@admin.register(PartyAddress)
class PartyAddressAdmin(admin.ModelAdmin):
    list_display = ('party', 'address')
    search_fields = ('party__party_name', 'address')

@admin.register(BOM)
class BOMAdmin(admin.ModelAdmin):
    list_display = ('bom_id', 'bom_name', 'produce_quantity')
    search_fields = ('bom_name',)

@admin.register(BOMItems)
class BOMItemsAdmin(admin.ModelAdmin):
    list_display = ('bom', 'item_name', 'quantity', 'rate')
    search_fields = ('bom__bom_name', 'item_name')