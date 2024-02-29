"""List All Policies with scope local (policy created locally by user/customer managed)

   Credits:
   - Original author: Parwiz Forogh  , udemy.com
   - Contributor: Girish Devappa
   - Date: Feb 29th 2024
"""

import boto3


def list_policies():
    """
    Create boto3 client for IAM
    using the client fetch the list of all policies
    """
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            # For each policy Print PolicyName and Arn
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print('Policy Name : {} Arn : {}'.format(policy_name, Arn))


list_policies()