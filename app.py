#!/usr/bin/env python3

from aws_cdk import (
    aws_cloudformation as cfn,
    core
)

from config import Config

from my_cdk_project.my_vpc_stack import MyVPCStack


app = core.App()
config = Config()
vpc = MyVPCStack(app, 'my-cdk-project', env=config.env, config=config.vpc())

app.synth()
