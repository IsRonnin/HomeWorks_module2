from django.urls import path
from .views import *



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('prod/', products, name="products"),
    path("try/", try_f),
    path("img/<str:name>", category_img),
    path('json/<int:id>', product_json_file_save_view)
]
