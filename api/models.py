from django.db import models

class Barcode(models.Model):
    id = models.AutoField(primary_key=True)
    barcode_number = models.CharField(max_length=255)
    barcode_type = models.CharField(max_length=50, default='TipoDesconhecido')
    data_escaneamento = models.DateTimeField(auto_now_add=True)