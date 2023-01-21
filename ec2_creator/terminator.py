import boto3
from datetime import date, datetime, timedelta


# function returns a list of running instances
def filtering_running():
    ec2 = boto3.resource('ec2', region_name="us-east-1")
    instances = ec2.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
                ]

            }

        ]
    )
    return list(instances)


# takes list of running instances and return new list with old instances
def make_instances_list_for_termination(list_instances):
    ec2 = boto3.client('ec2')
    new_list = []

    # for each instance
    for instance in list_instances:
        tags = ec2.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [instance.id]}])

        # for each tag in instance
        for tag in tags["Tags"]:

            # if has tag date. not is ignored
            if tag["Key"] == "Date":
                value_date = tag["Value"]

                # for instances with date tag check date. if date old add instance to new list
                if check_range_date(value_date):
                    new_list.append(instance)

    return new_list


# checks the date format. this function is used in check_range_date_function
def check_format_date(value_date):
    try:
        value_date = datetime.strptime(value_date, "%Y-%m-%d").date()
        return True, value_date
    except Exception:
        return False, value_date


# takes value date from make_instances_list_for_termination function. returns bool
def check_range_date(value_date):

    # making var date of limit date
    range_date = str(date.today() - timedelta(weeks=2))

    # calling twice for check_format_date function
    ques1, value_date = check_format_date(value_date)
    # call to check_format_date for range date to format it
    ques2, range_date = check_format_date(range_date)

    # if return bool
    if value_date <= range_date and ques1:
        return True
    else:
        return False


# main function of this module
def terminate_old_instances():

    # makes list of running instances
    instances = make_instances_list_for_termination(filtering_running())
    ques_bool = False

    # for each instance in list - terminate.
    for instance in instances:
        instance.terminate()
        print("instance " + instance.id + " terminated")
        ques_bool =True

    # if list is empty ques_bool stays false - print list is empty
    if not ques_bool:
        print("old instances list is empty ")

