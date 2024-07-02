import boto3

# Crear cliente para DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

response = dynamodb.delete_table(
        TableName='tabla-brayan-velez2'
    )



