from bucket import bucket 
from celery import shared_task

def get_obj_list_task():
    result = bucket.get_object_list()
    return result


# @shared_task
def delete_object_task(object_key):
    bucket.delete_object(object_key)
    
# @shared_task
def download_object_task(object_key):
    bucket.download_object(object_key)
    
'''
TODO:

def upload_object_task(object_key):
    bucket.upload_objects(object_key)
'''