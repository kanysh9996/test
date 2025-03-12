from django_filters import FilterSet
from .models import *

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'carmake' : ['exact'],
            'carmodel': ['exact'],
            'generation': ['exact'],
            'address_country': ['exact'],
            'address_city': ['exact'],
            'price': ['lt', 'gt'],
            'year': ['lt', 'gt'],
            'car_body': ['exact'],
            'drive': ['exact'],
            'transmission': ['exact'],
            'modification': ['lt', 'gt'],
            'engine': ['exact'],
            'state': ['exact'],
            'rule': ['exact'],
            'change': ['exact'],
            'register_country': ['exact'],
            'mileage': ['lt', 'gt'],
            'stock_kyrgyzstan': ['exact'],
            'customs_kyrgyzstan': ['exact'],


        }