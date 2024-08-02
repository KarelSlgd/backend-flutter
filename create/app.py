import pymysql
import json


def lambda_handler(event, context):

    body = json.loads(event['body'])
    nombre = body['nombre']
    fabricante = body['fabricante']
    autonomia = body['autonomia']
    velocidadMaxima = body['velocidadMaxima']

    connection = pymysql.connect(
        host='integradora.cf00oc48ct9r.us-east-1.rds.amazonaws.com',
        user='root',
        password='superroot',
        database='info'
    )

    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO auto (nombre, fabricante, autonomia, velocidadMaxima)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nombre, fabricante, autonomia, velocidadMaxima))
            connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
            },
            'body': json.dumps("Creado correctamente")
        }
    finally:
        connection.close()
