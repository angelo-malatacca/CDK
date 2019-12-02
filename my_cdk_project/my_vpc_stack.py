from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class MyVPCStack(core.Stack):

    def __init__(self, app: core.Construct, id: str, config: dict, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        self.vpc = ec2.Vpc(
            self, 'MyVpc',
            cidr='10.0.0.0/16',
            max_azs=99, # use all available AZs,
            subnet_configuration=[ 
               # { 'cidrMask': 28, 'name': 'nat', 'subnetType': ec2.SubnetType.PUBLIC },
                { 'cidrMask': 24, 'name': 'public-subnet', 'subnetType': ec2.SubnetType.PUBLIC },
                { 'cidrMask': 24, 'name': 'private-subnet', 'subnetType': ec2.SubnetType.PRIVATE }
            ],
        )

    def ref_vpc(self):
        return self.vpc