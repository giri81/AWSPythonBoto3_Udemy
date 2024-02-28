""" Update user
   Prerequisites: Run the script CreateUserAWS.py to create users

    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: Feb 28th 2024
"""

import boto3


def update_user(old_username, new_username):
    iam = boto3.client('iam')

    # using update_user method of client iam
    response = iam.update_user(
        UserName=old_username,
        NewUserName=new_username
    )

    print(response)


update_user('testuser', 'testuserUpdated')
