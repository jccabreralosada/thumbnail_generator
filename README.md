# Thumbnail Generator with AWS CloudFormation

The template generated for use in the AWS cloud is `serverless_thumbnail.yaml`. In the python folder is left the code used locally along with the image used for test purposes

## Description

This AWS CloudFormation template creates a thumbnail generator using AWS S3 and a Lambda function.

The architecture implemented on AWS via CloudFormation stands out for its simple and rapidly deployable approach, combining an S3 bucket for storing images with a Lambda function for automatic thumbnail generation. The automation of the Lambda function in response to load events in S3 generates an efficient and scalable process, coupled with security configuration through a specific role that protects data. In terms of cost, using a function that is activated only with the corresponding event when a new image is uploaded in the bucket saves costs by only charging for each call to the function, thus leaving the functionality on standby without generating additional costs.
However, there are areas for improvement, such as error handling to facilitate troubleshooting, the ability to customize the size and format of images as needed, and the implementation of metadata management for further analysis that could be generated. These improvements could make the architecture even more flexible and adaptive to various situations.


## Template Resources

The template creates the following resources:
- S3 Bucket (`BucketThumbnail`)
- Lambda Function (`Lambdathumbnail`)

## Prerequisites

- Have an Amazon Web Services account.
- Install and configure the AWS CLI.
- Configure AWS credentials with sufficient permissions.

Juan Camilo Cabrera Losada
