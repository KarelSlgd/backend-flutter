import pymysql
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    id = body['id']

    connection = pymysql.connect(
        host='integradora.cf00oc48ct9r.us-east-1.rds.amazonaws.com',
        user='root',
        password='superroot',
        database='info'
    )

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM auto WHERE id = %s"
            cursor.execute(sql, (id,))
            connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
            },
            'body': json.dumps('Eliminado correctamente')
        }
    finally:
        connection.close()
