# DAGOBAH - open source tool to generate internal threat intelligence, inventory & compliance data from AWS resources.

![alt text](https://github.com/Stuxend/dagobah/blob/master/images/dagobah-dashboard.png "Dagobah Inventory")

Dagobah is an open source tool written in python to automate the internal threat intelligence generation, inventory collection and compliance check from different AWS resources. Dagobah collects information and save the state into an elasticsearch index.

Dagobah runs into the a LAMBDA and looks at all the AWS REGIONS, actually collect differents configurations from: 

* EC2
* VPC
* ENI
* SecurityGroups

# DAGOBAH GOAL: 
- Add IOC and store them into elasticsearch/s3.
- Live centralized inventory/config information related to AWS/NON-AWS resources.
- Automatically evaluate resources against other platforms/analyzers.

# AWS services/resources:
- VPC
- EC2
- ENI
- Security Groups


# Non-AWS resources:
- WAZUH (comming soon)

# Code layout:
```sh
./
 |- dagobah.py (main control for manual/automated exec)
 |- modules/
             |- collector.py (query collection objects)
             |- iam_aws.py (iam stuff for aws multi account-role)
             |- setup.py (elk setup)
             |- analizer.py (analyzer for add external info to the collector)
```

# How works:


![alt text](https://github.com/Stuxend/dagobah/blob/master/images/deployment.png "Dagobah Inventory")

Ideally a Cloudwatch event is triggered the lambda every XXX with the account, role, and inventory type (all) to collect. The lambda gets the cloudwatch and iterates the accounts/role/inventory to start querying the AWS EC2 API with boto3 (not extra charges for use) and for different resources, an additional analyzer is triggered to get context information like: 
  - wazuh information (comming soon)
  - running time EC2
  - security group rule status (open/closed)
Each result is stored in the inventory index of elasticsearch. 



# Future integrations:
- lambda functions
- aws elb/nlb
- dns route53
- iam / trustadvisor
- s3 buckets
- eks/fargate
- transit-gateways
- api gateway
