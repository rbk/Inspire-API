import json

CORS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': True,
}

DATA = json.loads(open('quotes.json', 'r').read())

def all(event, context):
    response = {
        "statusCode": 200,
        "headers": CORS,
        "body": json.dumps(DATA)
    }
    return response

def one(event,context):
    qid = int(event['pathParameters']['id'])
    return {
        "statusCode": 200,
        "headers": CORS,
        "body": json.dumps(DATA[qid])
    }