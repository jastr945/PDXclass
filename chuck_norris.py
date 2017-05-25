'''A package called Requests
pip list
pip install requests
'''

# print(r.json()) # converts it into a Python-readable dictionary

# r = requests.get('http://api.icndb.com/jokes/random')
# json_data = r.json()
# print(json_data['value']['joke'])

import requests
package = {
    'APPID': '6b919e5d511686a6a70d2728794a6fe5',
    'q': str(input('Enter city: ')).upper()
}


r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

json_data = r.json()

print(r.url)
print(json_data['main']['temp'])
print((json_data['weather'][0])['description'])

