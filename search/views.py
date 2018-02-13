from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Class Based view
class SearchProductView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()


        """
        __icontains  = field that contains (doesn't matter capitalized letters)
        __iexact = field is exactly this
        """
