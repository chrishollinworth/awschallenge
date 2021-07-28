S3_BUCKET_NAME=$(cat three-tier-example/frontend/three-tier-example/src/config.json | jq -r '.[] | select(.OutputKey=="S3BucketName").OutputValue')
aws s3 rm s3://$S3_BUCKET_NAME --recursive
aws s3api delete-bucket --bucket $S3_BUCKET_NAME --region us-east-1
aws cloudformation delete-stack --stack-name test-three-tier-example --region us-east-1
