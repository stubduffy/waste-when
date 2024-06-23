import boto3
import json
import re
import os
from datetime import datetime

def publish_sms(message):
    client = boto3.client(
        'sns',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACESS_KEY'],
        region_name="eu-west-1"
    )

    response = client.publish(
        PhoneNumber=os.environ['PHONE'],
        Message=message,
    )
    print(response)

def month_string_to_int(string):
    if ("Jan" in string):
        return 1
    elif ("Feb" in string):
        return 2
    elif ("Mär" in string):
        return 3
    elif ("Apr" in string):
        return 4
    elif ("Mai" in string):
        return 5
    elif ("Jun" in string):
        return 6
    elif ("Jul" in string):
        return 7
    elif ("Aug" in string):
        return 8
    elif ("Sep" in string):
        return 9
    elif ("Okt" in string):
        return 10
    elif ("Nov" in string):
        return 11
    elif ("Dez" in string):
        return 12
    else:
        return 0

with open('cal.json') as file:
    file_contents = file.read()
    cal = json.loads(file_contents)
    for key in cal.keys():
        print(cal[key])
        split1 = re.split(r'\.', cal[key])
        split2 = re.split(r'[^0-9]+', split1[0])[1]
        split3 = re.split(r'\d+', split1[1])[0]
        split4 = re.split(r'[^0-9]+', split1[1])[1]
        day = int(split2)
        month = month_string_to_int(split3)
        year = int(split4)
        dt = datetime(day=day, month=month, year=year)
        print(dt)
        now = datetime.now()

        days_left = (dt - now).days
        if (days_left == 0):
            print("%s-müll tomorrow... publishing notification!" % key)
            publish_sms("" + key + "-müll collection tomorrow!!")
        else:
            print("still %s day(s) to go for %s-müll" % (days_left, key))        