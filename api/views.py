# views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Barcode
from .serializers import BarcodeSerializer
from PIL import Image
from pyzbar.pyzbar import decode


class BarcodeViewSet(viewsets.ModelViewSet):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer

    @action(detail=False, methods=['post'])
    def scan(self, request):
        image = request.FILES['image']
        barcode_number, barcode_type = self.decode_barcode(image)

        if barcode_number:
            barcode = Barcode(barcode_number=barcode_number,
                              barcode_type=barcode_type)
            barcode.save()
            serializer = BarcodeSerializer(barcode)
            return Response(serializer.data)
        
        else:
            return Response({'error': 'Não foi possível ler o número de barras.'}, status=400)

    def decode_barcode(self, image):
        image = Image.open(image)
        barcode_data = decode(image)

        if barcode_data:
            barcode_number = barcode_data[0].data.decode('utf-8')
            barcode_type = 'QRCode' if barcode_data[0].type == 'QRCODE' else 'Código de Barras'
            return barcode_number, barcode_type
        else:
            return None, None
