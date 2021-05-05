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



def doit(df, buck):
    create_bucket(buck, s3_connection)
    s3_client = boto3.client('s3')
        Filename=data, Bucket=buck, #or create_bucket_name(buck)
        Key=first_file_name) #?

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

#client
