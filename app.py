#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ai_use_case_2_python_cdk.ai_use_case_2_python_cdk_stack import AiUseCase2PythonCdkStack

from huggingface_sagemaker.huggingface_stack import HuggingfaceSagemaker


app = cdk.App()

# https://docs.aws.amazon.com/cdk/latest/guide/environments.htm
AiUseCase2PythonCdkStack(app, "AiUseCase2PythonCdkStack", 
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )

sagemaker = HuggingfaceSagemaker(app, "HuggingfaceServerlessSagemakerEndpoint", 
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )

app.synth()
