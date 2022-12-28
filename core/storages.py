from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.STATICFILES_LOCATION
    """Querystring auth must be disabled so that url() returns a consistent output."""
    querystring_auth = False
    file_overwrite = True
    default_acl = 'public-read-write'


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.MEDIAFILES_LOCATION
    querystring_auth = False
    default_acl = 'public-read-write'
