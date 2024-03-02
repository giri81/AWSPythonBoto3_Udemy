"""Create a IAM Role with trust policy
   only creating a role, no permission policy
    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: March 2nd 2024
"""

import boto3
import json

iam = boto3.client('iam')

role_name = "MyNewEC2Role"

# This trust policy allows EC2 instances to allow to assume this role
trust_policy = {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect":"Allow",
            "Principal": {
                "Service":"ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

iam.create_role(
    RoleName = role_name,
    AssumeRolePolicyDocument = json.dumps(trust_policy)


)

print(f"IAM Role {role_name} created")