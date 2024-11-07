from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=PLACE Your Web API KEY').read()
        json_data = json.loads(res)
        weather_data = {
            # "coordinate": str(json_data['coord']['lon']) + ' ' +str(json_data['coord']['lat']),
            'temperature': str(json_data['main']['temp'])+ 'K',
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city = ''
        weather_data = {}
    
    return render(request, 'index.html', {'city': city, "weather_data": weather_data})
