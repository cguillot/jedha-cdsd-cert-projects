variable "aws_region" {
  description = "storing of region from aws console"
  default     = "eu-west-3"
}

# Ensure you have configured a local profile with appropriate AWS credentials: aws configure --profile aws-admin
variable "aws_profile" {
  description = "local profile used when invoking aws configure"
  default     = "aws-admin"
}

variable "aws_key_pair_name" {
  description = "name of default EC2 key pair to provision"
  default     = "KEY-JEDHA-LEAD-FINAL-PROJECT"
}

variable "aws_allow_ssh_security_group" {
  description = "name of default security group to provision for SSH allowance"
  default     = "SG-JEDHA-LEAD-ALLOW-SSH"
}

variable "s3_bucket_name" {
  type    = string
  default = "jedha-fullstack-cert-projects-s3-bucket"
}

variable "user_name" {
  type    = string
  default = "jedha-fullstack-cert-projects-user"
}

locals {
  tags = {
    Owner   = "${var.user_name}"
    Project = "jedha-fullstack-cert-projects"
  }
}
