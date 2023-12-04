from django.urls import path
from .views import BarcodeViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView
    )


urlpatterns = [
    path('read-barcode/',
         BarcodeViewSet.as_view({'post': 'scan'}), name='read_barcode'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
         
]
