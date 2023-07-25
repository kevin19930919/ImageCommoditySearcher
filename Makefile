# Replace 'your-aws-account-id' with your AWS account ID
AWS_ACCOUNT_ID = 561307077992
# Replace 'your-region' with the AWS region where your ECR repository is located
AWS_REGION = ap-southeast-1
# Replace 'image-commodity-searcher' with the name of your ECR repository
ECR_REPO = kevintsai

# Build the Docker image
build:
	docker build -t $(ECR_REPO):latest .

# Tag the Docker image with ECR repository URI
tag:
	docker tag $(ECR_REPO):latest $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO):latest

# Authenticate Docker to your ECR
login:
	aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com

# Push the Docker image to ECR
push: login tag
	docker push $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO):latest
