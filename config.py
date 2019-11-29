from aws_cdk import core

class Config():

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.env=core.Environment(
            account='234873931226',
            region='eu-central-1'
        )

    def vpc(self):
        __config={
        }
        return __config