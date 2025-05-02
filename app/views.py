from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProductMaster, BOM, BOMItems, JobCard
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta, date

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

@api_view(['POST'])
def create_bom(request):
    serializer = BOMSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def create_bomItems(request):
    serializer = BOMItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["GET"])
def machine_master_list(request):
    machines = MachineMaster.objects.all()
    serializer = MachineMasterSerializer(machines, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product_master(request):
    product = ProductMaster.objects.all()
    serializer = ProductMasterSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bom_Items(request):
    BOMItems = BOMItems.objects.all()
    serializer = BOMItemsSerializer(BOMItems, many=True)
    return Response(serializer.data)

@csrf_exempt
def report_by_date(request):
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({"error": "Date is required"}, status=400)

    job_cards = JobCard.objects.filter(date=date_str).select_related("machine_name")

    data = [
        {
            "date": jc.date,
            "machine_name": jc.machine_name.name_of_machine,
            "machine_capacity": jc.machine_name.machine_capacity,
            "operator_name": jc.operator_name,
            "quantity_made": jc.product_qty,
        }
        for jc in job_cards
    ]

    return JsonResponse({"data": data})


@csrf_exempt
def report_by_operator(request):
    operator_names = request.GET.getlist('operator')
    if not operator_names:
        return JsonResponse({"error": "Operator name(s) required"}, status=400)

    today = date.today()
    last_week = today - timedelta(days=7)

    job_cards = JobCard.objects.filter(
        date__range=[last_week, today],
        operator_name__in=operator_names
    ).select_related("machine_name").order_by("date")

    data = [
        {
            "date": jc.date,
            "operator_name": jc.operator_name,
            "machine_name": jc.machine_name.name_of_machine,
            "machine_capacity": jc.machine_name.machine_capacity,
            "quantity_made": jc.product_qty,
        }
        for jc in job_cards
    ]

    return JsonResponse({"data": data})
