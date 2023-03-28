from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect, FileResponse
from .models import Product, Category, Order
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .forms import OrderForm
import json, datetime

def get_product(id: int):
    try:
        return Product.objects.get(pk=id)
    except Product.DoesNotExist:
        print(id)
        raise Http404
    
def get_category(name: str):
    try:
        print(Category.objects.all())
        return Category.objects.get(name=name)
    except Exception as e:
        print(e)
        print(name)
        raise Http404
    
@csrf_exempt
def products(request: HttpRequest):
    if request.method == "POST":
        body = json.loads(request.body.decode('UTF-8'))

        category = get_category(body["category"])

        product = Product(
            name = body["name"],
            category = category,
            price = body["price"],
            animal = body["animal"],
            weight = body["weight"],
            release_date = datetime.datetime.strptime(body["release_date"], "%d.%m.%Y")
        )
        product.save()
        
        return HttpResponse(str(product))

    
    elif request.method == "GET":
        category_name = request.GET.get("category")
        
        products = Product.objects.all()
        if category_name is not None and category_name.strip() != '':
            category = Category.objects.filter(name__icontains = category_name).first()
            if category is None:
                products = products.filter(~Q(name__icontains = ""))
            else:
                products = products.filter(category = category)

        return render(request, 'products.html', {"title": "Макасин", "products": products})
    
def product_view(request: HttpRequest, id: int):
    product = get_product(id)
    if request.method == "GET":
        if product.name is None:
            return redirect(reverse('products'))
        #return HttpResponse(str(product))
        return render(request, 'product.html', {"title": product.name, "product": product})
    

def try_f(request: HttpRequest):
    return HttpResponse("Try!")

def category_img(request: HttpRequest, name: str):
    try:
        img = f"media/{Category.objects.get(name = name).image}"
    except:
        img = None
    
    if img is None:
        raise Http404()
    return FileResponse(
        open(img, 'rb'),
        as_attachment=True
    )

def product_json_file_save_view(request: HttpRequest, id:int):
    product = get_product(id)
    product.to_json()

    return FileResponse(open(f'zoomag/dumps/{id}.json', 'rb'), as_attachment=True)

def index(request: HttpRequest):
    return render(request, 'index.html', {"title": "zoomag"})

@csrf_exempt
def make_order(request: HttpRequest, id: int):
    data =        { 'title': "Оформление заказа",
                    'form': OrderForm(),
                    'product': get_product(id),
                    'error': ''
                  }
    if request.method == "GET":
        return render(request, 'make_order.html', data)
                  
    elif request.method == "POST":
        form = OrderForm(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect(reverse('products'))            
        try:
            Order(**form.cleaned_data, product = get_product(id)).save()

        except Exception:
            data['error'] = 'Ошибка при сохранении заказа'
            data['form'] = form
        return HttpResponseRedirect(reverse("product", kwargs={'id': id}))
    return HttpResponse(status=405)