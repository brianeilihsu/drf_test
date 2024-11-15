import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price']) #(model_data, fields=['id', 'title', 'price', 'sale_price']) if you want specific data
        data = ProductSerializer(instance).data
    return Response(data)