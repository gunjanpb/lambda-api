#!/usr/bin/env python3

import json
import os
from typing import Optional

import boto3
s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get('BUCKET_NAME')


def list_s3_bucket_contents(bucket_name, folder_name='') -> Optional[list]:
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    folder_name = folder_name.removesuffix('/') + '/'
    if 'Contents' in response:
        objects = set( obj['Key'].removeprefix(folder_name).split('/',1)[0] 
                      for obj in response['Contents'] if obj['Key'] != folder_name
        )
        return list(objects)
    else:
        return None   # no such folder


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    folder_name = (event['pathParameters'] or {} ) .get('folder', '')
    contents = list_s3_bucket_contents(BUCKET_NAME, folder_name)
    if contents is None:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"No such folder {folder_name} in S3 bucket {BUCKET_NAME}"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"contents": contents})
    }
    
