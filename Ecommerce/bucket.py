import boto3
from django.conf import settings
import logging
from botocore.exceptions import ClientError


class Bucket:
    
    
    def __init__(self):
        
        self.s3_resource = boto3.resource(
            's3',
            endpoint_url = settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        )
        
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        self.bucket = self.s3_resource.Bucket(self.bucket_name)
        
        """  
        creating a new bucket if it's needed 
         
        Code Snippet:
        try:
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            bucket = s3_resource.Bucket(bucket_name)
            bucket.create(ACL='public-read')
            
        except ClientError as exc:
            logging.error(exc)
        """
    
    def get_object_list(self):
        return [obj for obj in self.bucket.objects.all()]
        
    def delete_object(self, object_key):
        object = self.bucket.Object(object_key)
        object.delete()
        return True
    
    def download_object(self, object_key):
        self.bucket.download_file(object_key, settings.AWS_LOCAL_STORAGE + object_key)
    '''
    TODO: 
    
    def upload_objects(self, object_key):
        with open(settings.AWS_LOCAL_STORAGE, 'rb') as file:
            self.bucket.put_object(ACL="private", Body=file, Key=object_key)
            
    '''
        
bucket = Bucket()
        
