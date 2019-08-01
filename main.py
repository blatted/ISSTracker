import json
import turtle
import urllib.request
import time
from geopy.geocoders import Nominatim





def getISSastronauts():
    url='http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print('People in Space: ', result['number'])
    people = result['people']
    for p in people:
        print(p['name'] + ' in ' + p['craft'])

def showISS():

    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('lat =  ', lat, ' long= ', lon)
    flat = float(lat)
    flon = float(lon)
    screen = turtle.Screen()
    screen.setup(1480, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    #iss.setheading(90)

    iss.penup()
    iss.goto(flon, flat)
    whenISSAboveMe(screen)
    screen.onkeypress(showISS)
    screen.listen()
    screen.mainloop()

def whenISSAboveMe(screen):
    address = screen.textinput("When is the ISS above this address?", "Please enter an address: ")
    geolocator = Nominatim(user_agent="ISSTracker")
    location = geolocator.geocode(address)
    print(location.address)
    print(location.latitude, location.longitude)
    url = "http://api.open-notify.org/iss-pass.json"
    url = url + '?lat=' + str(location.latitude) + '&lon=' + str(location.latitude)
    response = urllib.request.urlopen(url)
    result = json.loads(response.read()) 
    over = result['response'][1]['risetime']
    style = ('Arial',6,'bold')
    print(time.ctime(over))
    

showISS()