from django.shortcuts import render, get_object_or_404, redirect
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


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    # Check if this product is already in the user's cart
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        # If already exists, increase quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('home')