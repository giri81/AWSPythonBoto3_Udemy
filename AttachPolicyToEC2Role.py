"""Attach S3 get object access Policy to EC2 role

    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: March 2nd 2024
"""

import boto3

iam = boto3.client("iam")

role_name = "MyNewEC2Role"

policy_name = "MyNewECPolicy"

# Copy ARN from AWS  console
iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = ""
)

print(f"Polic {policy_name} attached to IAM Role {role_name}")

