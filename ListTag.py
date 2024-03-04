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

response = iam_client.list_users()

for user in response['Users']:
    user_name = user['UserName']
    tags = iam_client.list_user_tags(UserName=user_name)['Tags']
    print(f"User : {user}, Tags : {tags}")