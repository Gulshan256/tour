from django.shortcuts import render
from .models import destinations


# Create your views here.

def index(request):

    # if request.method =='POST':
    #     dest=destinations()
    #     name=request.POST.get('name')
    #     image=request.POST.get('image')
    #     desc=request.POST.get('desc')
    #     price=request.POST.get('price')
    #     offer=request.POST.get('offer')
        
    #     dest=destinations(name=name, image=image, desc=desc, price=price, offer=offer)
    #     dest.save()
    hh=destinations.objects.all()

    return render(request, "index.html",{"dd":hh})



