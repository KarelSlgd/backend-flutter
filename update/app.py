import pymysql
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    id = body['id']
    nombre = body.get('nombre')
    fabricante = body.get('fabricante')
    autonomia = body.get('autonomia')
    velocidadMaxima = body.get('velocidadMaxima')

    connection = pymysql.connect(
        host='integradora.cf00oc48ct9r.us-east-1.rds.amazonaws.com',
        user='root',
        password='superroot',
        database='info'
    )

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE auto SET "
            updates = []
            values = []

            if nombre is not None:
                updates.append("nombre = %s")
                values.append(nombre)
            if fabricante is not None:
                updates.append("fabricante = %s")
                values.append(fabricante)
            if autonomia is not None:
                updates.append("autonomia = %s")
                values.append(autonomia)
            if velocidadMaxima is not None:
                updates.append("velocidadMaxima = %s")
                values.append(velocidadMaxima)

            sql += ", ".join(updates) + " WHERE id = %s"
            values.append(id)
            cursor.execute(sql, tuple(values))
            connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
            },
            'body': json.dumps('Actualización correctamente')
        }
    finally:
        connection.close()
