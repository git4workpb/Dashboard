from rest_framework import viewsets
from app.models import ProductMaster, MachineMaster, JobCard, PartyMaster, PartyAddress, BOM, BOMItems
from app.serializers import ProductMasterSerializer, MachineMasterSerializer, JobCardSerializer, PartyMasterSerializer, PartyAddressSerializer, BOMSerializer, BOMItemsSerializer
class ProductMasterViewSet(viewsets.ModelViewSet):
    queryset = ProductMaster.objects.all()
    serializer_class = ProductMasterSerializer

class MachineMasterViewSet(viewsets.ModelViewSet):
    queryset = MachineMaster.objects.all()
    serializer_class = MachineMasterSerializer

class JobCardViewSet(viewsets.ModelViewSet):
    queryset = JobCard.objects.all()
    serializer_class = JobCardSerializer

class PartyMasterViewSet(viewsets.ModelViewSet):
    queryset = PartyMaster.objects.all()
    serializer_class = PartyMasterSerializer

class PartyAddressViewSet(viewsets.ModelViewSet):
    queryset = PartyAddress.objects.all()
    serializer_class = PartyAddressSerializer

class BOMViewSet(viewsets.ModelViewSet):
    queryset = BOM.objects.all()
    serializer_class = BOMSerializer

class BOMItemsViewSet(viewsets.ModelViewSet):
    queryset = BOMItems.objects.all()
    serializer_class = BOMItemsSerializer