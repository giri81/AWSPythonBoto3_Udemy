"""Attach policy to the user

    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: March 2nd 2024
"""

import boto3


def attach_policy(policy_arn, username):
    """
    Create boto3 client for IAM
    using the client to attach policy
    """
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

    print(response)

# Replace arn param with actual arn of custom policy
attach_policy('arn:aws:iam::aws:policy/AmazonRDSFullAccess', 'testuser')
