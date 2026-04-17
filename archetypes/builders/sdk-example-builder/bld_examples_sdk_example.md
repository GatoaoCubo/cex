---
kind: examples
id: bld_examples_sdk_example
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of sdk_example artifacts
quality: 8.9
title: "Examples Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, examples]
tldr: "Golden and anti-examples of sdk_example artifacts"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
title: "AWS S3 File Upload with Boto3"
language: python
vendor: Amazon Web Services
description: "Uploads a file to an S3 bucket using AWS SDK for Python (Boto3)"
```

```python
import boto3
import os

def upload_to_s3(file_path, bucket_name, object_key):
    """Upload file to S3 bucket."""
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise
```

## Anti-Example 1: Missing Error Handling
```python
import boto3

def upload_to_s3(file_path, bucket_name, object_key):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{object_key}")
```

## Why it fails
No exception handling leaves the application vulnerable to crashes from network errors, permission issues, or invalid inputs. Missing error feedback makes debugging impossible.

## Anti-Example 2: Hardcoded Credentials
```python
import boto3

def upload_to_s3(file_path, bucket_name, object_key):
    s3_client = boto3.client('s3', aws_access_key_id='AKIAXXXXXXXXXXXXXXXX',
                             aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    s3_client.upload_file(file_path, bucket_name, object_key)
```

## Why it fails
Hardcoding credentials violates security best practices. It exposes sensitive information in code repositories and increases risk of credential leakage. Proper approach uses environment variables or IAM roles.
