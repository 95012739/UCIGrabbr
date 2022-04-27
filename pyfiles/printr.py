#Download some packages
import uuid as ud
import boto3 as b3
import os
import pandas

def doit(df, buck, object_name = None):
    
    df = pandas.DataFrame(df)
    
    cwd = os.getcwd()

    path = cwd + "\mojdata.csv"

    #make sure we have one path and create it if it doesn't exist
    if os.path.exists(path):
        os.remove(path)

    #get our data in a csv with the right name
    df.to_csv(path)

    #stick it in a bucket
    s3_client = b3.client('s3')
    bucket_name = create_bucket_name(buck)
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                              'LocationConstraint': 'us-east-2'})

    if object_name is None:
        object_name = "file"
        
    #Upload
    s3_client.upload_file(path, bucket_name, object_name)

    return True

#creates an S3 bucket name 
def create_bucket_name(bucket_prefix):
    i = 7
#The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(ud.uuid4())])


