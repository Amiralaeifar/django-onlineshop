from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from . import tasks
from django.contrib import messages


class HomeView(View):
    
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {
            'products': products
        })


class ProductDetailView(View):
    
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detail.html', {
            'product': product,
        })
        
        
class BucketHome(View):
    template_name = 'home/bucket.html'
    
    
    def get(self, request):
        objects = tasks.get_obj_list_task()
        return render(request, self.template_name, {
            'objects': objects,
        })
        
        
class BucketDeleteObject(View):
    
    def get(self, request, object_key):
        tasks.delete_object_task(object_key) # tasks.delete_object_task.delay(object_key)
        messages.success(request, 'deleted successfully', 'success')
        return redirect('home:bucket')
    
    
class BucketDownloadObject(View):
    
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