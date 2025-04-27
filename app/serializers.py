from rest_framework import serializers
from .models import ProductMaster, MachineMaster, JobCard, PartyMaster, PartyAddress, BOM, BOMItems

class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaster
        fields = '__all__'

class MachineMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineMaster
        fields = '__all__'

class JobCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCard
        fields = '__all__'

class PartyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyMaster
        fields = '__all__'

class PartyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyAddress
        fields = '__all__'

class BOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM
        fields = '__all__'

class BOMItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItems
        fields = '__all__'
        
class MachineMasterGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineMaster
        fields = ['name_of_machine','product_name']