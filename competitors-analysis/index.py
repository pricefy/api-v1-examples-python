'''
https://developers.pricefy.io/#operation--analysis-competitors--country--get
'''

import requests

api_key = 'your-api-key'
country_code = 'IT' # the country code you want to analyse
headers = {'Authorization': 'Bearer '+api_key}
url = 'https://api.pricefy.io/v1/analysis/competitors/'+country_code
r = requests.get(url, headers=headers)
print r.json()