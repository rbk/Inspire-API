"""Inspire API."""
import json
from random import randint

CORS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': True,
}

DATA = json.loads(open('quotes.json', 'r').read())
ENDPOINT = 'https://inspire.richardkeller.net'
"""
views
votes
request count by api key
request source
"""


def check(key):
    """Return true if valid else auth error object."""
    return True


def one(event, context):
    """Quote by id."""
    qid = int(event['pathParameters']['id'])
    DATA[qid]['id'] = qid
    DATA[qid]['link'] = ENDPOINT + '/api/quotes/' + str(qid)
    return {
        "statusCode": 200,
        "headers": CORS,
        "body": json.dumps(DATA[qid])
    }


def rand(event, context):
    """Random quote."""
    num = randint(0, len(DATA) - 1)
    DATA[num]['id'] = num
    DATA[num]['link'] = ENDPOINT + '/api/quotes/' + str(num)
    return {
        "statusCode": 200,
        "headers": CORS,
        "body": json.dumps(DATA[num])
    }
