from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from . import tasks
from django.contrib import messages
from utils import IsAdminMixins


class HomeView(View):
    
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/home.html', {
            'products': products,
            'categories': categories,
        })


class ProductDetailView(View):
    
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detail.html', {
            'product': product,
        })
        
        
class BucketHome(IsAdminMixins, View):
    template_name = 'home/bucket.html'
    
    
    def get(self, request):
        objects = tasks.get_obj_list_task()
        return render(request, self.template_name, {
            'objects': objects,
        })
        
        
class BucketDeleteObject(IsAdminMixins, View):
    
    def get(self, request, object_key):
        tasks.delete_object_task(object_key) # tasks.delete_object_task.delay(object_key)
        messages.success(request, 'deleted successfully', 'success')
        return redirect('home:bucket')
    
    
class BucketDownloadObject(IsAdminMixins, View):
    
    def get(self, request, object_key):
        tasks.download_object_task(object_key) # tasks.download_object_task.delay(object_key)
        messages.success(request, 'downloaded successfully', 'success')
        return redirect('home:bucket')
        
'''
TODO:

class BucketUploadView(View):
    
    def get(self, request, object_key):
        tasks.upload_object_task(object_key)
        messages.success(request, 'uploaded successfully', 'success')
        return redirect('home:bucket')
'''