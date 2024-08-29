#!/usr/bin/env python3
import os

import aws_cdk as cdk

from huggingface_sagemaker.huggingface_stack import HuggingfaceSagemaker


app = cdk.App()

sagemaker = HuggingfaceSagemaker(app, "HuggingfaceServerlessSagemakerEndpoint", 
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )

app.synth()
