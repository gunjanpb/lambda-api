# lambda-api
A simple AWS Lambda function accessible via API Gateway.


## Testing
> python3 -m pip install -r requirements.txt

> pytest


## Deploy

Suitable to be deployed in AWS free tier.

Provide AWS credentials in one of the usual ways, verify variables.tf, and execute:
> terraform apply

This will print:
> api_route = "https://<some_id>.execute-api.ap-south-1.amazonaws.com/v1/list-bucket-content"

You may then add content to the bucket and use this endpoint to list files/folders.

```shell
gunjan@FocalUbuntu:~/python workspace/lambda-api$ curl $api_route
{"contents": ["dir1", "dir2"]}
gunjan@FocalUbuntu:~/python workspace/lambda-api$ curl $api_route/dir2
{"contents": ["file2", "file1"]}
gunjan@FocalUbuntu:~/python workspace/lambda-api$ curl $api_route/whatever
{"error": "No such folder whatever in S3 bucket gunjantest"}
gunjan@FocalUbuntu:~/python workspace/lambda-api$ 
```

A demo is available at https://rzyq4xmmvg.execute-api.ap-south-1.amazonaws.com/v1/list-bucket-content


## Tear down
> terraform destroy

You may need to empty the bucket first.


## Design decisions
- Lambda has:
  - latest python runtime with boto3
  - easy to grant permissions to bucket
  - easy logging via CloudWatch
- API Gateway has:
  - good integration with Lambda (Lambda Proxy Integration)
  - public, https endpoint


## Projects that made this easier:
- [Terraformer](https://github.com/GoogleCloudPlatform/terraformer):  
  Creates basic terraform stubs from existing AWS resources, as a starting point.  
  Note: Generated files have hardcoded ids. You need to define dependencies yourself.  
  Note: liberally use `terraform import` command to actually import resources into tfstate.
- [pytest](https://pytest.org):
  Use familiar `assert` to write test cases. Auto detect test cases.
  