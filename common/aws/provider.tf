terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0" # Use latest compatible AWS provider version
    }
  }
}

# Credentials should be either in ~/.aws/credentials or env vars [AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_REGION,AWS_PROFILE]
provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}
