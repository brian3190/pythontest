import requests
baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID':'notmykeyad7ceca67905860fd432987d6fc404db','q':'Seattle,US'}
response = requests.get(baseUrl, params=parameters)
print(response.content)
