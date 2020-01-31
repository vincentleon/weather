import pyowm
API_key = '1d558f088ecb162ac1fc6c705ff081b5'
owm = pyowm.OWM(API_key)
observation = owm.weather_at_place('Rennes,FR')
w = observation.get_weather()
#print(w)

temperature = w.get_temperature(unit='celsius')
status = w.get_detailed_status()

print("current temperature : ", temperature['temp'], "°C")
print("current status : ",status)

fc = owm.three_hours_forecast('Rennes,fr')
f = fc.get_forecast()

for w in f: 
    print(w)
