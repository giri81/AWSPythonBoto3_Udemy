""" Add Tag to IAM user
    Tag are key:value acts as meta deta
    Useful in labeling users based on dept, proj etc.

    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: March 4th 2024
"""

import boto3

iam_client = boto3.client('iam')

user_name = 'testuserUpdated'

tags = [{'Key':'Department', 'Value':'HR'}, {'Key':'Project', 'Value':'Onboarding'}]

iam_client.tag_user(UserName=user_name, Tags=tags)

print('Tag Added')