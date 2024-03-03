"""Create Instance Profile
    Thi8 is container for IAM role that you can use to pass information.
    Another way to associate a rule with EC2 instance.
    When EC2 instance is launched , it assumes the Role's permissions.

    Credits:
    - Original author: Parwiz Forogh  , udemy.com
    - Contributor: Girish Devappa
    - Date: March 3rd 2024
"""

import boto3

iam = boto3.client('iam')

instance_profile_name = "MyNewEC2Profile"

iam.create_instance_profile(
    InstanceProfileName = instance_profile_name
)

print(f"Instance Profile Created {instance_profile_name}")
