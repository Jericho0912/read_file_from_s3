import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name=''  # e.g., 'us-west-2'
)

# Create an S3 client
s3 = session.client('s3')

# Specify the bucket and the file key
bucket_name = 'arduinodaybucket'
file_key = 'myKey'

# Get the file object
file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)

# Read the file content
file_content = file_obj['Body'].read().decode()

print(file_content)
