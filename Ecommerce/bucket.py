import boto3
from django.conf import settings
import logging
from botocore.exceptions import ClientError


class Bucket:
    
    def __init__(self):
        #logging.basicConfig(level=logging.INFO)
        self.s3_resource = boto3.resource(
            's3',
            endpoint_url = settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        )
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        self.bucket = self.s3_resource.Bucket(self.bucket_name)
        
        """   
        try:
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            bucket = s3_resource.Bucket(bucket_name)
            bucket.create(ACL='public-read')
            
        except ClientError as exc:
            logging.error(exc)
        """
    
    def get_objects(self):
        objects = self.bucket.objects.all()
        return objects
    
    def get_object_list(self):
        l = []
        for obj in self.bucket.objects.all():
            l.append(obj)
        return l
        
        
bucket = Bucket()
        