output "bucket_arn" {
  value = aws_s3_bucket.main_s3_bucket.arn
}


output "bucket_name" {
  value = aws_s3_bucket.main_s3_bucket.bucket
}

# output "bucket_acl" {
#   value = aws_s3_bucket.main_s3_bucket.acl
# }

output "user_id" {
  value = aws_iam_user.project_iam_user.id
}

# output "rendered_policy" {
#   value = aws_iam_policy.project_s3_bucket_policy.json
# }
output "user_secret" {
  value = aws_iam_access_key.project_iam_user_key.encrypted_secret
}

output "user_access_key_id" {
  value = aws_iam_access_key.project_iam_user_key.id
}

output "user_access_key_secret" {
  value     = aws_iam_access_key.project_iam_user_key.secret
  sensitive = true
}
