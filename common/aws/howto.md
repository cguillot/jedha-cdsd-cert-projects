# Provisionning Terraform

Ensure you own an admin IAM. If not gather one from your AWS subscription.
Then, run following commands from shell within the devcontainer.

AWS provisionning profile:
```bash
# Configure AWS profile used for provisionning
aws configure --profile aws-admin

# Validate
aws sts get-caller-identity --profile aws-admin
```

Terraform provisionning:
```bash
cd  /workspaces/jedha-cdsd-cert-projects/common/aws/

# Initialize you local terraform
terraform init

# Validate
terraform validate

# Deploy/Sync (enter "yes" when asked to deploy)
terraform apply
```

Environment udpate:
```bash
cd  /workspaces/jedha-cdsd-cert-projects/common/aws/

# Execute following command
terraform output -json | jq -r '"CDSD_AWS_ACCESS_KEY_ID=" + (.user_access_key_id.value) + "\nCDSD_AWS_SECRET_ACCESS_KEY=" + (.user_access_key_secret.value | tostring) + "\nCDSD_S3_BUCKET_NAME=" + (.bucket_name.value)'

# Copy output to your ".env" file
```
