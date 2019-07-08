# # reportWeather.py - print weather report.
#
import datetime
import json
import requests
#
APP_KEY = '12345'  # Obtain yours from: http://openweathermap.org/
#
#
def time_converter(time):

    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time

#
def url_builder_name(city_name):

    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?q='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + city_name + '&lang=zh_cn' + '&units=' + unit + '&APPID=' + APP_KEY
    return full_api_url
#
#
def data_fetch(full_api_url):
#
    response = requests.get(full_api_url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))

    return json.loads(response.text)
#
#
def data_organizer(raw_data):
#
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = {
        'city': raw_data.get('name'),
        'country': sys.get('country'),
        'temp': main.get('temp'),
        'temp_max': main.get('temp_max'),
        'temp_min': main.get('temp_min'),
        'humidity': main.get('humidity'),
        'pressure': main.get('pressure'),
        'sky': raw_data['weather'][0]['main'],
        'sunrise': time_converter(sys.get('sunrise')),
        'sunset': time_converter(sys.get('sunset')),
        'wind': raw_data.get('wind').get('speed'),
        'wind_deg': raw_data.get('deg'),
        'dt': time_converter(raw_data.get('dt')),
        'cloudiness': raw_data.get('clouds').get('all'),
		'description': raw_data['weather'][0]['description']
    }
    return data
#
#
def data_output(data):
#
#     # °C
    data['m_symbol'] = '\u00b0' + 'C'
#
    s = '''
----------------------------------------------
    Current weather in: {city}, {country}:
    {temp}{m_symbol} {sky}
    Max: {temp_max}, Min: {temp_min}

    Wind Speed: {wind}, Degree: {wind_deg}
    Humidity: {humidity}
    Cloud: {cloudiness}
    Pressure: {pressure}
    Sunrise at: {sunrise}
    Sunset at: {sunset}
    Description: {description}

    Last update from the server: {dt}
----------------------------------------------'''
    print(s.format(**data))
#
#
city = input('Which city you want to check? ')
#
url = url_builder_name(city)
rawData = data_fetch(url)
prettyData = data_organizer(rawData)
data_output(prettyData)

