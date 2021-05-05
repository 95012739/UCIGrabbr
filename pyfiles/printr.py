import uuid
import boto3
import pandas
import beautifulsoup4
import requests
import functools

def compose(*funcs):
    """
    Functional composition
    
    [f, g, h] will be f(g(h(x)))
    """
    def compose_two(f, g):
        def c(x):
            return f(g(x))
        return c
    return functools.reduce(compose_two, funcs)

#pick one
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def doit(df, buck):
    reate_bucket(buck, s3_connection)


#creates an S3 bucket name 
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

#creates the bucket
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

#input name
#create bucket bucket name
#file path

#upload file with one of below
#object
s3_resource.Object(first_bucket_name, first_file_name).upload_file(
    Filename=first_file_name)

#first object
first_object.upload_file(first_file_name)

#resource
s3_resource.Bucket(first_bucket_name).upload_file(
    Filename=first_file_name, Key=first_file_name)

#client
s3_resource.meta.client.upload_file(
    Filename=first_file_name, Bucket=first_bucket_name,
    Key=first_file_name)