from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product

# Create your views here.

# Class Based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
            context = super(ProductListView, self).get_context_data(*args, **kwargs)
            print(context)
            return context

# Function Based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
            context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
            print(context)
            return context

# Function Based view
def product_detail_view(request, pk):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    try:
        instance = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404("Product Does Not Exist!!!!")
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
