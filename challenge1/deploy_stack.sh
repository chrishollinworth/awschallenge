aws s3api create-bucket --bucket aws-sam-cli-managed-default-samclisourcebucket-testthreetier --region us-east-1 
sam build --template three-tier-example/backend/three-tier-example.yaml
sam deploy --template-file .aws-sam/build/template.yaml --s3-bucket aws-sam-cli-managed-default-samclisourcebucket-testthreetier --capabilities CAPABILITY_IAM --stack-name test-three-tier-example --region us-east-1 --parameter-overrides ParameterKey=SiteBucketName,ParameterValue=testthreetier

python3 load_data.py
aws cloudformation describe-stacks --query Stacks[].Outputs[] --region us-east-1 --output json > three-tier-example/frontend/three-tier-example/src/config.json
cd three-tier-example/frontend/three-tier-example/
npm run build
S3_BUCKET_NAME=$(cat src/config.json | jq -r '.[] | select(.OutputKey=="S3BucketName").OutputValue')
aws s3 cp build s3://$S3_BUCKET_NAME/ --recursive
WEBSITE_URL=$(cat src/config.json | jq -r '.[] | select(.OutputKey=="DomainName").OutputValue')
echo 'Site now live at: https://'$WEBSITE_URL