resource "aws_s3_bucket" "main_s3_bucket" {
  bucket = var.s3_bucket_name
  tags   = local.tags
}

resource "aws_iam_policy" "project_s3_bucket_policy" {
  name        = "jedha_fullstack_cert_projects_s3_bucket_policy"
  description = "S3 policy for JEDHA Fullstack cert projects user(s)"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect : "Allow",
        Action : [
          "s3:GetBucketLocation",
          "s3:ListAllMyBuckets"
        ],
        Resource : "arn:aws:s3:::*"
      },
      {
        Effect = "Allow"
        Action = [
          "s3:*"
        ]
        Resource = [
          "${aws_s3_bucket.main_s3_bucket.arn}/*",
          "${aws_s3_bucket.main_s3_bucket.arn}"
        ]
      }
    ]
  })
}

# Allow the user to tag instance when creating it only
# Only allowed to modify instances he tagged

# {
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Action": [
#          "ec2:RunInstances"
#       ],
#       "Resource": "*"
#     },
#     {
#       "Effect": "Allow",
#       "Action": [
#          "ec2:CreateTags"
#       ],
#       "Resource": "arn:aws:ec2:region:account:*/*",
#       "Condition": {
#          "StringEquals": {
#              "ec2:CreateAction" : "RunInstances"
#           }
#        }
#     }
#   ]
# }
# "arn:aws:ec2:::*"
# "ForAnyValue:StringEquals": {
#   "aws:TagKeys": ["Owner"]
# }

resource "aws_iam_policy" "project_ext_policy" {
  name = "jedha_fullstack_cert_projects_ext_policy"
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : "iam:GetUser",
        "Resource" : "*"
      }
    ]
  })
}


# {
# "Version": "2012-10-17",
# "Statement": [
# {
# "Effect": "Allow",
# "Action": [
# "ec2:*",
# "s3:*",
# "cloudfront:*",
# "cloudwatch:*",
# "elasticloadbalancing:*",
# "iam:CreateServiceLinkedRole"
# ],
# "Resource": "*",
# "Condition": {
# "StringEquals": {
# "aws:RequestedRegion": "ap-southeast-1"
# }
# }
# },
# {
# "Effect": "Deny",
# "Action": "ec2:*",
# "Resource": "*",
# "Condition": {
# "ForAnyValue:StringNotLike": {
# "ec2:InstanceType": [
# "t2.micro"
# ]
# }
# }
# }
# ]
# }
# jedha_lead_final_project_

resource "aws_iam_user" "project_iam_user" {
  name = var.user_name
}

# Create the access key
resource "aws_iam_access_key" "project_iam_user_key" {
  user = aws_iam_user.project_iam_user.name
}

resource "aws_iam_user_policy_attachment" "iam_policy_attachment" {
  user       = aws_iam_user.project_iam_user.name
  policy_arn = aws_iam_policy.project_s3_bucket_policy.arn
}

resource "aws_iam_user_policy_attachment" "iam_ext_policy_attachment" {
  user       = aws_iam_user.project_iam_user.name
  policy_arn = aws_iam_policy.project_ext_policy.arn
}
