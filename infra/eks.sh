#! /usr/bin/env bash

eksctl create cluster --name=kafka8s --managed --spot --instance-types=m5.xlarge \
    --nodes=2 --alb-ingress-access --node-private-networking --region=us-east-2 \
    --nodes-min=2 --nodes-max=3 --full-ecr-access --asg-access --nodegroup-name=ng-kafka8s