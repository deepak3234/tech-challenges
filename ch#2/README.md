******Query Metadata of an instance within AWS******

Script that will query the meta data of an instance within AWS and provide a JSON formatted output.


Approach:

The IMDS service of AWS has been queried there through _AWS CLI_. The specific key retrieval part is being performed through python script with required key as input.


Prerequisites:

1.	AWS CLI configured
2.	Python3


Execute the script using following steps:

1.	Configure the AWS subscription

    #aws configure

2.	Get the metadata of an instance stored in a file using AWS CLI and passing instance id of the EC2 machine

    #aws ec2 describe-instances --instance-ids {instance-id of your ec2 instance} > ec2metadata.json
     
    Note- The file given here is for sample purpose. It needs to be generated with same name 
          and at same path for the script to work for another ec2 instance.

3.	Go to the src folder and execute the _metadataquery.py_ script by passing the input at its execution. 


Output: 

The script output would be somewhat like the one below:

![image](https://user-images.githubusercontent.com/81134005/122902004-b9f90c00-d36b-11eb-8986-5c93a71eea92.png)

