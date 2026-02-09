# Youtube-Sentiments-Insight

uv venv --python 3.11

source .venv/bin/activate

ub init

uv add -r requirements.txt --upgrade

uv pip install -e .

## DVC

dvc init

dvc repro

dvc dag


## AWS

aws congigure


## 3. Create ECR repo to store/save docker image 
- save the URI: 591789164360.dkr.ecr.us-east-2.amazonaws.com/mlproj

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## 6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one


## 7. Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-2

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app

