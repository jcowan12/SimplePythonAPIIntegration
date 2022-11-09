import requests
import json
import webbrowser

#API KEY
API_KEY = '7fgq7qFmPkUS11nJiPhGTNKAxCs4E3fEiorpFZOf'

#API URL
url = 'https://api.nasa.gov/planetary/apod'

#Parameters
params= {
    'api_key' : API_KEY,
    'hd' : 'True',
    'date' : '2022-11-9'
}

response = requests.get(url, params = params)
json_data = json.loads(response.text)
#print(json_data)

image_url = json_data['hdurl']
webbrowser.open(image_url)