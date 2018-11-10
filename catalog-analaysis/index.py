'''
https://developers.pricefy.io/#operation--analysis-catalog--country---id--get
'''

import requests

api_key = 'your-api-key'
country_code = 'IT' # the country code you want to analyse
product_ean = '3175681126213'
headers = {'Authorization': 'Bearer '+api_key}
url = 'https://api.pricefy.io/v1/analysis/catalog/'+country_code+'/EAN:'+product_ean
r = requests.get(url, headers=headers)
print r.json()