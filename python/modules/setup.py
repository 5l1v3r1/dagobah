import logging
import os
from datetime import datetime
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import urllib3

##### define standard configurations ####

# SETUP LOGGIN OPTIONS
log = logging.getLogger("daobah-inventory-setup")
log.setLevel(logging.INFO)
# SETUP DATATIME FOR NOW
datetime_now = datetime.now()
urllib3.disable_warnings()

#Setup AWS ElasticAuth.
awsauth = AWS4Auth(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'], os.environ['AWS_REGION'], 'es',
                   session_token=os.environ['AWS_SESSION_TOKEN'])

#Setup for ELK general connection
def sendToELK(data):
        log.info(str(datetime_now)+" starting sendtoelk function")
        index_name = 'inventory-' + datetime_now.strftime("%Y-%m-%d")
        elk_node = os.environ['elk_node']
        es = Elasticsearch(
                hosts=[{'host': elk_node, 'port': 443}],
                http_auth=awsauth,
                use_ssl=True,
                verify_certs=False,
                connection_class=RequestsHttpConnection,
                timeout=60,
                max_retries=10,
                retry_on_timeout=True
                )
        log.info(str(datetime_now)+" sending logs now")
        es.index(index=index_name, body=data)
        log.info(str(datetime_now)+" done")