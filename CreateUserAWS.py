"""Create a new non-root IAM in a AWS account user
   List all users
   Prerequisites: Understand the IAM user create workflow.
                  Create a AWS Key via AWS management console for programmatic access in your root AWS account
                  Using Boto3 package
    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: Feb 28th 2024
"""

import boto3


def createuser(username):
    # Create a IAM client
    iam = boto3.client('iam')

    # Create a response from IAM client
    response = iam.create_user(UserName=username)

    print(response)


createuser('testuser')


# Verify the UserId and the Arn created for 'testuser', Http response code for 200
# Verify the 'testuser' in your AWS console

def all_users():
    iam = boto3.client('iam')

    # Paginator of IAM client for listing users
    paginator = iam.get_paginator('list_users')

    # Using the paginator interface, iterate the items
    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print('Username : {} Arn : {}'.format(username, Arn))


all_users()
