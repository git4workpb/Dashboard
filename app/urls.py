from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from app.views.model_viewsets import ProductMasterViewSet, MachineMasterViewSet, JobCardViewSet, PartyMasterViewSet, PartyAddressViewSet, BOMViewSet, BOMItemsViewSet

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
]