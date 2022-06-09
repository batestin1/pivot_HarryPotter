#! /usr/bin/env bash



aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 079775608725.dkr.ecr.us-east-2.amazonaws.com
docker build -t kafka-repository .
docker tag kafka-repository:latest 079775608725.dkr.ecr.us-east-2.amazonaws.com/kafka-repository:latest
docker push 079775608725.dkr.ecr.us-east-2.amazonaws.com/kafka-repository:latest