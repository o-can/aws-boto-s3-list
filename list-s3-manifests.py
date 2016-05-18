import os

import boto3

# Simple script to get the key of an object from S3
# Matches a given prefix and returns the key with the newest last modified timestamp.

boto3.setup_default_session(region_name=os.getenv('AWS_DEFAULT_REGION', 'eu-central-1'))

# Create an S3 Client
client = boto3.client('s3')
bucketname = "<bucketname>"
prefix = "<prefix>"

# Fetch all keys from the bucket that are matching the prefix
response = client.list_objects_v2(
    Bucket=bucketname,
    Prefix=prefix
)

# Just grab the key + last modified from the response and store the tuples in a list
key_repo = []
for key in response['Contents']:
    entry = (key['Key'], key['LastModified'])
    key_repo.append(entry)

# Sort the list by datetime(second entry), reverse the order to have the newest first
# Print the key of the newest entry
if len(key_repo) > 0:
    key_repo.sort(key=lambda x: x[1], reverse=True)
    print(key_repo[0][0])
