from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product

# Create your views here.

# Class Based view
class ProductListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
            context = super(ProductListView, self).get_context_data(*args, **kwargs)
            print(context)
            return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

# Function Based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"
    def get_context_data(self, *args, **kwargs):
            context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
            print(context)
            return context
    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        pk      = self.kwargs.get('pk')
        print(pk)
        instance = Product.objects.get_by_id(pk)
        print(instance)
        if instance is None:
            raise Http404("Product Does Not Exist!!!!")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk      = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)



# Function Based view
def product_detail_view(request, pk):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     raise Http404("Product Does Not Exist!!!!")
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product Does Not Exist!!!!")
    #
    # qs = Product.objects.filter(id=pk)
    #
    # if qs.exists() and qs.count() == 1: #len of queryset, to confirm that it's unique
    #     instance = qs.first()
    #     print(instance)
    # else:
    #     raise Http404("Product Doesn't Exist!!!!")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
