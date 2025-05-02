from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views_folder
from app.views_folder.model_viewsets import ProductMasterViewSet, MachineMasterViewSet, JobCardViewSet, PartyMasterViewSet, PartyAddressViewSet, BOMViewSet, BOMItemsViewSet
from .views import report_by_date, report_by_operator

router = DefaultRouter()
router.register(r'product-master', ProductMasterViewSet)
router.register(r'machine-master', MachineMasterViewSet)
router.register(r'job-card', JobCardViewSet)
router.register(r'party-master', PartyMasterViewSet)
router.register(r'party-address', PartyAddressViewSet)
router.register(r'bom', BOMViewSet)
router.register(r'bom-items', BOMItemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('report-by-date/', report_by_date),
    path('report-by-operator/', report_by_operator),
]