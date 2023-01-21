import boto3
from datetime import date
import terminator


# reading user_data file
def read_data_user_file():
    with open(r'user_data.sh', 'r') as file:
        data = file.read()
        return data


# reads configurations file returns only vaules
def read_configurations_file():
    with open(r'configurations.txt', 'r') as file:

        list_lines_file = []

        for line in file:
            list_lines_file.append(line)

        type_in = list_lines_file[0].partition(":")[2][:-1]
        name = list_lines_file[1].partition(":")[2][:-1]
        image = list_lines_file[2].partition(":")[2][:-1]
        sec_group_id = list_lines_file[3].partition(":")[2]

        return type_in, name, image, sec_group_id


# create security group - used once to create. from then on security group id is mentioned in config file
def create_security():
    name = input(print("write new name of security group"))
    print("group name: "+name)
    ec2 = boto3.client('ec2')

    # create the security group
    secgroup = ec2.create_security_group(
        GroupName=name,
        Description='exs.py creation'
    )

    # security group id
    security_group_id = secgroup['GroupId']

    # opening ports 22, 443, and 80
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 443, 'ToPort': 443, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )

    return security_group_id


# create one instance
def create_instance(num_web):

    type_in, name, image, sec_group_id = read_configurations_file()

    ec2 = boto3.resource('ec2', region_name='us-east-1')

    instances = ec2.create_instances(
        ImageId=image,
        MinCount=1,
        MaxCount=1,
        InstanceType=type_in,
        UserData=read_data_user_file(),
        SecurityGroupIds=[sec_group_id],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name + str(num_web)
                    },
                    {
                        'Key': 'Date',
                        'Value': str(date.today())
                    },
                ]
            },
        ]

        )

    for instance in instances:
        print("new instance created : " + instance.id + " " + instance.private_ip_address)
    return instance


# create a multiple instances with suitable names and returns a list of instances
def create_instances(num):
    list_instances = []
    # for loop calls the create instance function
    for i in range(1, num+1):
        instance = create_instance(i)
        list_instances.append(instance)
    return list_instances


# main function
def main():

    # create one instance web1
    create_instances(1)

    # calling terminator module to terminate old instances
    terminator.terminate_old_instances()


main()