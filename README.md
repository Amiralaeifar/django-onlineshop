# django Online Shop
------

_project overview_:

+ Custom User model & Custom manager
+ Personalizing admin panel fieldsets and forms
+ cleaned out email and phone_number to be unique
+ verify users via sms using Kavenegar API
+ managing media files in buckets using ARVAN Cloud Storages
+ AWS Service __s3_simple storage service__
+ managing bucket contents __(list objects, delete and download)__ with boto3 SDK
+ personalized management command
+ receiving aware datetime in commands, using pytz module
+ celery beat for asynchronous tasks
+ __daemonization__ using _supervisor_ for celery and celery_beat
+ __bootstrap__ in templates
+ __cart__ , the ability of adding or removig product to cart, easy purchase
+ set __permissions__ for orders
+ __context processors__ in orders
+ payments with __Zarinpal__ for orders
+ __discount coupon__ and field lookups
+ override *get_form* func for admin panel
+ cache system with __Redis__ 
+ __ckeditor__ for description on product, manual setup with full toolbar






