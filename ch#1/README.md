Build a 3 Tier Application

A three-tier architecture is a software architecture pattern where the application is broken down into three logical tiers: the presentation layer, the business logic layer, and the data storage layer. This architecture is used in a client-server application such as a web application that has the frontend, the backend, and the database. Each of these layers or tiers does a specific task and can be managed independently of each other.

image

Here, AWS services is being used to design and build a three-tier cloud infrastructure: Elastic Compute Cloud (EC2), Auto Scaling Group, Virtual Private Cloud (VPC), Elastic Load Balancer (ELB), Security Groups and the Internet Gateway. This infrastructure will be designed through Terraform and will be highly available and fault tolerant.

Approach:

Designed here is the infrastructure with one VPC with 4 subnets with combination of private and public for various layers. In addition to that there will be a bastion host and a NAT gateway for the admins to have access to the infrastructure.

Prerequisites:

Terraform v0.14 or earlier.
Valid AWS Subscription
Provision all resources with Terraform:

Go to 3-tier-components folder

#cd 3-tier-components

Run terraform init

#terraform init

Run terraform fmt and validate

#terraform fmt #terraform validate

Apply the resources

#terraform apply

Once done, resources can be removed by destroying them

#terraform destroy

Output:

You would see something like this

On Terraform -

image

On AWS Console -

image

Reference:

For building a 3-tier application, the basic architecture reference has been taken from https://medium.com/the-andela-way/designing-a-three-tier-architecture-in-aws-e5c24671f124.
