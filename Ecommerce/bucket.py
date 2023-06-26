import boto3
from django.conf import settings
import logging
from botocore.exceptions import ClientError


class Bucket:
    
    def __init__(self):
        #logging.basicConfig(level=logging.INFO)
        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url = settings.AWS_S3_ENDPOINT_URL,
                aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
            )
        except Exception as exc:
            logging.info(exc)
            
        """   
        try:
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            bucket = s3_resource.Bucket(bucket_name)
            bucket.create(ACL='public-read')
            
        except ClientError as exc:
            logging.error(exc)
            """
    
    def get_objects(self):
        for bucket in self.s3_resource.buckets.all():
            return bucket
        
        
        
bucket = Bucket()
        