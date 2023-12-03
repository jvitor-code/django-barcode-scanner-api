from django.urls import path
from .views import BarcodeViewSet

urlpatterns = [
    path('read-barcode/',
         BarcodeViewSet.as_view({'post': 'scan'}), name='read_barcode'),
]
