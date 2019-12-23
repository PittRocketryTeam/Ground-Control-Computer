import requests
import json

class weatherAPI():
    name = ""
    locKey = 0

    def __init__(self):
        pass

    def setLocation(self,lat, lon):
        req = requests.get(
            "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=56maHeR2yA2OJAHG8ArAgAsaV77Ui52e&q="+str(lat) +"%2C"+str(lon))
        raw = json.loads(req._content)
        print(raw)
        self.locKey = raw['Key']
        self.name = raw['LocalizedName']


    def getData(self):
        wReq = requests.get(
            "http://dataservice.accuweather.com/currentconditions/v1/"+str(self.locKey)+"?apikey=56maHeR2yA2OJAHG8ArAgAsaV77Ui52e&details=true")
        
        raw = json.loads(wReq.content)
  
        data = {
            'WeatherText': raw[0]['WeatherText'],
            'Temperature': raw[0]['Temperature']['Imperial']['Value'],
            'WeatherIcon': raw[0]['WeatherIcon'],
            'WindDirection': raw[0]['Wind']['Direction']['Localized'],
            'WindSpeed': raw[0]['Wind']['Speed']['Imperial']['Value'],
            'CloudCover': raw[0]['CloudCover'],
            'Ceiling': raw[0]['Ceiling']['Imperial']['Value'],
            'Link': raw[0]['Link'],
            'Name' : self.name
        }

        return data
    
