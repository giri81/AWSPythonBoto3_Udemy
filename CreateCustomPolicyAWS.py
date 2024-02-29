"""Create custom policy with admin access
    Verify: In AWS console, under IAM dashboard the policy count is incremented by 1.

    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: Feb 29th 2024
"""


import boto3
import json


def create_policy():
    """
    Create boto3 client for IAM
    using the client create user policy
    """
    iam = boto3.client('iam')

    user_policy = {
        "Version":"2012-10-17",
        "Statement":[
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    """
    Create policy
    :param PolicyName
    :param PolicyDocument, json document policy
    :return: response
    """
    response = iam.create_policy(
        PolicyName = 'pyFullAccess',
        PolicyDocument=json.dumps(user_policy)
    )

    print(response)


create_policy()