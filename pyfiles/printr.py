#Download required packages
import uuid as ud
import boto3 as b3
import os
import pandas

def doit(df, buck, object_name=None):
    """
    Uploads a Pandas DataFrame to an S3 bucket after converting it to a CSV file.

    Parameters:
    - df: Pandas DataFrame, the data to upload.
    - buck: str, the bucket name where the data will be uploaded.
    - object_name: str, optional, the name of the object (file) in the bucket. Default is None.

    Returns:
    - bool: True if the upload is successful.
    """
    
    # Convert input to a Pandas DataFrame
    df = pandas.DataFrame(df)
    
    # Get the current working directory
    cwd = os.getcwd()

    # Create a path for the CSV file
    path = cwd + "\\mojdata.csv"

    # Ensure there's no existing file at the path and create the file
    if os.path.exists(path):
        os.remove(path)

    # Save the DataFrame to a CSV file at the specified path
    df.to_csv(path)

    # Initialize an S3 client
    s3_client = b3.client('s3')

    # Create a unique bucket name
    bucket_name = create_bucket_name(buck)

    # Create the S3 bucket with a specified location constraint
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                              'LocationConstraint': 'us-east-2'})

    # If object_name is not provided, set it to "file"
    if object_name is None:
        object_name = "file"
        
    # Upload the CSV file to the S3 bucket
    s3_client.upload_file(path, bucket_name, object_name)

    # Return True to indicate successful upload
    return True

def create_bucket_name(bucket_prefix):
    """
    Generates a unique S3 bucket name.

    Parameters:
    - bucket_prefix: str, prefix to use for the bucket name.

    Returns:
    - str: A unique bucket name.
    """
    # We'll append a random UUID to the bucket_prefix to ensure uniqueness
    return ''.join([bucket_prefix, str(ud.uuid4())])


