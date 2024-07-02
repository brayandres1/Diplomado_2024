import boto3

# Crear cliente para DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

tabla = dynamodb.Table('tabla-brayan-velez')

# Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '1'})

print(response['Item'])

# Leer todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])


    
tabla.put_item(Item={
    "id": "4",
    "nombre": "Velez",
    "ciudad": 'Bogotá',
    "edad": 34
})


# Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '4'})

print("elemento antes de actualizar", response['Item'])

response = tabla.update_item(
    Key={
        'id': '3'  
    },
    UpdateExpression='SET edad = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': 34  # Nuevo valor para atributo2
    }
)

response = tabla.get_item(Key={'id': '4'})

print("elemento despues de actualizar", response['Item'])
