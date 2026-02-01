from django.shortcuts import render
from .models import CafeShop
# Create your views here.
def cafe_map(request):
    cafes = CafeShop.objects.filter(is_active=True)
    context = {
        'cafes': cafes
    }
    return render(request, 'cafes/map.html', context)