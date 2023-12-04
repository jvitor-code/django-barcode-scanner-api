from rest_framework import serializers
from .models import Barcode

class BarcodeSerializer(serializers.ModelSerializer):
    data_escaneamento = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    class Meta:
        model = Barcode
        fields = ['id', 'barcode_number', 'barcode_type', 'data_escaneamento']