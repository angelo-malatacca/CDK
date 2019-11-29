#!/usr/bin/env python3

from aws_cdk import core

from my_cdk_project.my_cdk_project_stack import MyCdkProjectStack


app = core.App()
MyCdkProjectStack(app, "my-cdk-project")

app.synth()
