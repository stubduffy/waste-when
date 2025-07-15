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
        matcher = re.compile('\D+(\d+)\.(\D+)(\d\d\d\d)')
        m = matcher.match(cal[key])
        if m:
            day = int(m.groups()[0])
            month = month_string_to_int(m.groups()[1])
            year = int(m.groups()[2])
        else:
            raise Exception("Sorry, couldnt decipher the date string")
        dt = datetime(day=day, month=month, year=year)
        print(dt)
        now = datetime.now()

        days_left = (dt - now).days
        if (days_left == 0):
            print("%s-müll tomorrow... publishing notification!" % key)
            publish_sms("" + key + "-müll collection tomorrow!!")
        else:
            print("still %s day(s) to go for %s-müll" % (days_left, key))        
