from django.urls import path, include
from . import views

app_name = 'home'

bucket_urls = [
    path('', views.BucketHome.as_view(), name='bucket'),
    path('delete_obj_bucket/<str:object_key>', views.BucketDeleteObject.as_view(), name='bucket_delete_object'),
    path('download_obj_bucket/<str:object_key>', views.BucketDownloadObject.as_view(), name="bucket_download_object"),
    #TODO:  path('upload_obj_bucket/<str:object_key>', views.BucketUploadView.as_view(), name="bucket_upload_object"),
]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
