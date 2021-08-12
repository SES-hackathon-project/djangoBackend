import requests
import json

def yelprequest(location,budget,term):
    apikey = 'Dxz1i3z3sUG-WHABDTt3spqrkNXbG9_WJWd6we8CRKJXlWXK_XhkZhG5fx3LfLkTm8hCJg0npHjbEoD4_MKHArYROdAoXJ5dnEWJ0hjYek7WehEW5acXb5Uz8poUYXYx'
    url = 'https://api.yelp.com/v3/businesses/search'
    head = {'Authorization': 'Bearer %s' % apikey}

    parameters = {
                'term':term,
                'location': location,
                'price': budget,
                'radius': 10000,
                'limit': 30
                }

    response = requests.get(url, params = parameters, headers = head)

    data = response.json()
    
    for business in data['businesses']:
        print(business['name'])
    

yelprequest('Washington DC',2,'movies')