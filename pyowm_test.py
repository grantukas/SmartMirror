import pyowm

owm = pyowm.OWM('1819a58f535dffa60f13ee3f3e8ebcfa')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('92866,us')
w = observation.get_weather()

# Forecast test
fc = owm.three_hours_forecast('92866,us')
forecast = fc.get_forecast()
wlist = forecast.get_weathers()

weather = wlist[0]

temp_min_list = []
for w in forecast:
    print(w.get_reference_time(timeformat='iso'))
    print(w.get_temperature('fahrenheit'))
    print('\n')

#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
#print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
#print(w.get_humidity())              # 87
#print(w.get_temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#print(w.get_temperature('fahrenheit'))

temp_dict = w.get_temperature('fahrenheit')
print(w.get_reference_time(timeformat='iso'))


curr_temp = temp_dict['temp']
max_temp = temp_dict['temp_max']
min_temp = temp_dict['temp_min']
status = w.get_status()
detailed_status = w.get_detailed_status()
icon_url = w.get_weather_icon_url()
weather_code = w.get_weather_code()
#result = re.search('asdf=5;(.*)123jasd', s)

print("Current Temp: {} °F".format(curr_temp))
print("Low Temp: {} °F".format(min_temp))
print("High Temp: {} °F".format(max_temp))
print(status)
print(detailed_status)
print(weather_code)

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)
