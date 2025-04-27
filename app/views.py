from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProductMaster
from .serializers import *

@api_view(['POST'])
def create_product(request):
    serializer = ProductMasterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_machine(request):
    serializer = MachineMasterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_jobcard(request):
    serializer = JobCardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_party(request):
    serializer = PartyMasterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["GET"])
def machine_master_list(request):
    machines = MachineMaster.objects.all()
    serializer = MachineMasterSerializer(machines, many=True)
    return Response(serializer.data)