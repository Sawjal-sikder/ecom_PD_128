from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):

      products = Product.objects.all()
    
      context = {
            'products':products,
      }
      return render(request, 'home.html', context)


def product_details(requst, slug):
      product = get_object_or_404(Product, slug=slug)
      context = {
            'product': product,      }
      return render(requst, 'product_details.html',context)

def search_procducts(request):
      if request.method == 'POST':
            search_query = request.POST.get('search')
            product_search = Product.objects.filter(name__icontains=search_query)

            context = {
                  'products': product_search,
            }
            return render(request, 'home.html', context)
      return render(request, 'home.html')