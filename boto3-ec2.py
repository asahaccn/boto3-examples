import boto3  

    # Define the desired instance type
DESIRED_INSTANCE_TYPE = 't2.micro'

    # Define other EC2 instance parameters
AMI_ID = 'your-ami-id'  # Example AMI ID (e.g., Amazon Linux 2 AMI)
KEY_NAME = 'your-key-name'  # Replace with your key pair name
SECURITY_GROUP_IDS = ['your-security-group-id']  # Replace with your security group ID(s)
REGION_NAME = 'us-east-1' # Replace with your desired AWS region
SubnetId= 'your-subnetid'

def create_ec2_instance_if_t2_micro():
        """
        Creates an EC2 instance only if the instance type is t2.micro.
        """
        if DESIRED_INSTANCE_TYPE != 't2.micro':
            print(f"Instance creation aborted: Instance type is not '{DESIRED_INSTANCE_TYPE}'.")
            return

        try:
            ec2 = boto3.client('ec2', region_name=REGION_NAME)

            print(f"Attempting to create a {DESIRED_INSTANCE_TYPE} EC2 instance...")
            response = ec2.run_instances(
                ImageId=AMI_ID,
                InstanceType=DESIRED_INSTANCE_TYPE,
                MinCount=1,
                MaxCount=1,
                KeyName=KEY_NAME,
                SecurityGroupIds=SECURITY_GROUP_IDS,
                SubnetId=SubnetId,
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'Name', 'Value': f'My-{DESIRED_INSTANCE_TYPE}-Instance-4'},
                        ]
                    },
                ]
            )

            instance_id = response['Instances'][0]['InstanceId']
            print(f"EC2 instance '{instance_id}' of type '{DESIRED_INSTANCE_TYPE}' created successfully.")

        except Exception as e:
            print(f"Error creating EC2 instance: {e}")

if __name__ == '__main__':
        create_ec2_instance_if_t2_micro()



# if we give DESIRED_INSTANCE_TYPE = 't2.xyz' output will be Instance creation aborted: Instance type is not 't2.xyz'.
