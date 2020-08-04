import logging
import boto3
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timezone
import os

# SETUP LOGGIN OPTIONS
log = logging.getLogger("daobah-inventory-analizer")
log.setLevel(logging.INFO)
# SETUP DATATIME FOR NOW
datetime_now = datetime.now()

def analizer_expose_sg(data):
    log.info(str(datetime_now)+" starting the expose sg analizer")
    sg_status = 'closed'
    full_access = "0.0.0.0/0"
    for permission in data:
        for ip in permission['IpRanges']:
                for cidr in ip['CidrIp']:
                    if ip['CidrIp'] == full_access:
                        sg_status = 'open'
    log.info(str(datetime_now)+" done sg analizer")
    return(sg_status)

def analizer_launch_days(data):
    log.info(str(datetime_now)+" starting the launch days count analizer")
    if data !='':
        diff_time = datetime.now(timezone.utc) - data
    else:
        diff_time = 'n/a'
    log.info(str(datetime_now)+" done count analizer")
    return(diff_time.days)