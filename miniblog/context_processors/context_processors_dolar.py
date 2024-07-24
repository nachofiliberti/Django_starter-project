import requests
from django.core.cache import cache

from product.models import Product

def dolar_exchange_rates(request):
    #busco en cache
    exchange_rates = cache.get('exchange_rates')
    #si no encuentro
    if exchange_rates is None:
        #llamo a la api y le asigno a una variable el json 
        exchange_rates = requests.get("https://dolarapi.com/v1/dolares").json()
        #guardo en cache
        cache.set('exchange_rates', exchange_rates, 600)
        #devuelvo el json
    return dict(
        valores_dolar=exchange_rates
    )

