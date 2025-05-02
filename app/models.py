from django.db import models
import uuid

class ProductMaster(models.Model):
    product_item_name = models.CharField(max_length=255, primary_key=True)
    category = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    opening_stock = models.FloatField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_item_name


class MachineMaster(models.Model):
    name_of_machine = models.CharField(max_length=255, primary_key=True)
    machine_process_name = models.CharField(max_length=500)
    mould = models.CharField(max_length=255, blank=True, null=True)
    machine_capacity = models.FloatField()
    machine_final_produce_product_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name_of_machine
    
class ShiftType(models.TextChoices):
    DAY = 'DAY', 'Day Shift'
    NIGHT = 'NIGHT', 'Night Shift'

class JobCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique primary key using UUID
    date = models.DateField()
    machine_name = models.ForeignKey('MachineMaster', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_qty = models.FloatField()
    operator_name = models.CharField(max_length=255, default="")
    shift = models.CharField(max_length=10, choices=ShiftType.choices,default=ShiftType.DAY,)

    def __str__(self):
        return f"Job Card - {self.date} - {self.machine_name.name_of_machine}"
    
class PartyMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique primary key using UUID
    party_name = models.CharField(max_length=255)

    def __str__(self):
        return self.party_name
    
class PartyAddress(models.Model):
    party = models.ForeignKey(PartyMaster, on_delete=models.CASCADE, related_name='address')
    address = models.TextField()

    def __str__(self):
        return f"Address for {self.party.party_name}"

    

class BOM(models.Model):
    bom_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique primary key using UUID
    bom_name = models.CharField(max_length=255)
    produce_quantity = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.bom_name

class BOMItems(models.Model):
    bom = models.ForeignKey(BOM, on_delete=models.CASCADE, related_name='bom_items')  # One-to-Many relationship with BOM
    item_name = models.CharField(max_length=255)
    quantity = models.FloatField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name