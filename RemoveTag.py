""" List Tag of IAM user
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

tag_keys = ['Department', 'Project']

iam_client.untag_user(UserName=user_name, TagKeys=tag_keys)