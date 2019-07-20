import json

DATA = json.loads(open('quotes.json', 'r').read())

print(DATA[1])