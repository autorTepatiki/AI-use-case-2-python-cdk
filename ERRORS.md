ERRORS

Failed resources:
HuggingfaceServerlessSagemakerEndpoint | 10:15:36 | CREATE_FAILED        | AWS::SageMaker::Endpoint       | SagemakerEndpoint/hf_endpoint (SagemakerEndpointhfendpointE7336632) The role 'arn:aws:iam::894985317171:role/HuggingfaceServerlessSage-hfsagemakerexecutionrole6-tWeiyTzeD2Tp' does not have BatchGetImage permission for the image: '763104351884.dkr.ecr.sa-east-1.amazonaws.com/huggingface-pytorch-inference:1.9.1-transformers4.12.3-cpu-py38-ubuntu20.04'.

 ❌  HuggingfaceServerlessSagemakerEndpoint failed: Error: The stack named HuggingfaceServerlessSagemakerEndpoint failed creation, it may need to be manually deleted from the AWS console: ROLLBACK_COMPLETE: The role 'arn:aws:iam::894985317171:role/HuggingfaceServerlessSage-hfsagemakerexecutionrole6-tWeiyTzeD2Tp' does not have BatchGetImage permission for the image: '763104351884.dkr.ecr.sa-east-1.amazonaws.com/huggingface-pytorch-inference:1.9.1-transformers4.12.3-cpu-py38-ubuntu20.04'.
    at FullCloudFormationDeployment.monitorDeployment (C:\Users\cerna\AppData\Roaming\npm\node_modules\aws-cdk\lib\index.js:447:10567)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async Object.deployStack2 [as deployStack] (C:\Users\cerna\AppData\Roaming\npm\node_modules\aws-cdk\lib\index.js:450:200276)
    at async C:\Users\cerna\AppData\Roaming\npm\node_modules\aws-cdk\lib\index.js:450:181698

 ❌ Deployment failed: Error: The stack named HuggingfaceServerlessSagemakerEndpoint failed creation, it may need to be manually deleted from the AWS console: ROLLBACK_COMPLETE: The role 'arn:aws:iam::894985317171:role/HuggingfaceServerlessSage-hfsagemakerexecutionrole6-tWeiyTzeD2Tp' does not have BatchGetImage permission for the image: '763104351884.dkr.ecr.sa-east-1.amazonaws.com/huggingface-pytorch-inference:1.9.1-transformers4.12.3-cpu-py38-ubuntu20.04'.
    at FullCloudFormationDeployment.monitorDeployment (C:\Users\cerna\AppData\Roaming\npm\node_modules\aws-cdk\lib\index.js:447:10567)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async Object.deployStack2 [as deployStack] (C:\Users\cerna\AppData\Roaming\npm\node_modules\aws-cdk\lib\index.js:450:200276)
    at async C:\Users\cerna\AppData\Roaming\npm\node_modules\aws-cdk\lib\index.js:450:181698

The stack named HuggingfaceServerlessSagemakerEndpoint failed creation, it may need to be manually deleted from the AWS console: ROLLBACK_COMPLETE: The role 'arn:aws:iam::894985317171:role/HuggingfaceServerlessSage-hfsagemakerexecutionrole6-tWeiyTzeD2Tp' does not have BatchGetImage permission for the image: '763104351884.dkr.ecr.sa-east-1.amazonaws.com/huggingface-pytorch-inference:1.9.1-transformers4.12.3-cpu-py38-ubuntu20.04'.
