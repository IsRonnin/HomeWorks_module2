
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', start_page, name="start_page"),
    path('products/', products, name='products'),
    path('products/product/<int:id>', product, name='product'),
    path('img', image_view, name='image'),
    path('json/<int:id>', json_view, name='json'),
    path('categories/<str:category>', get_img_category, name = 'category'),
    path('categories/', get_all_categories, name="all_categories")
    #path('lits')

]