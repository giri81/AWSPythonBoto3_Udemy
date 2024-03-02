"""Create policy
    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: March 2nd 2024
"""

import boto3
import json

iam = boto3.client('iam')

policy_name = "MyNewECPolicy"

# This policy allows the role to perform S3 get object
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::girish-devappa-1/*"
        }
    ]
}

iam.create_policy(
    PolicyName=policy_name,
    PolicyDocument = json.dumps(policy_document)
)

print("Policy Created")