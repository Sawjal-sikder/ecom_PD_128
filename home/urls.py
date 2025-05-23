from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('product/details/<slug:slug>/', product_details, name='product_details'),
    path('search/procducts/', search_procducts, name='search_procducts'),
    path('add/to/cart/<int:id>/', add_to_cart, name='add_to_cart'),
]
