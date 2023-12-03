from rest_framework import serializers
from .models import Barcode

class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ['id', 'barcode_number', 'barcode_type', 'scanned_at']