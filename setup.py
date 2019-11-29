import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="my_cdk_project",
    version="0.0.1",

    description="A simple CDK infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Angelo Malatacca",

    package_dir={"": "my_cdk_project"},
    packages=setuptools.find_packages(where="my_cdk_project"),

    install_requires=[
        "aws-cdk.core==1.18.0",
        "aws-cdk.aws-cloudformation==1.18.0",
        "aws-cdk.aws_ec2==1.18.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
