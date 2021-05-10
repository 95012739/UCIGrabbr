



def doit(df, buck, object_name = None):
    s3_client = b3.client('s3')
    bucket_name = create_bucket_name(buck)
    s3_client.create_bucket(Bucket=bucket_name)

    if object_name is None:
        object_name = "file"

    response = s3_client.upload_file(df, bucket_name, object_name)

    return True

#creates an S3 bucket name 
def create_bucket_name(bucket_prefix):
    i = 7
#The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(ud.uuid4())])



#input name
#create bucket bucket name
#file path

#upload file with one of below
#object

#client
