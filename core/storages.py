from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.STATICFILES_LOCATION
    # custom_domain = False
    # querystring_auth = False
    # file_overwrite = True
    # default_acl = 'public-read-write'
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        # self.custom_domain = settings.STATIC_S3_CUSTOM_DOMAIN
        super().__init__(*args, **kwargs)


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.MEDIAFILES_LOCATION
    # querystring_auth = False
    # default_acl = 'public-read-write'
