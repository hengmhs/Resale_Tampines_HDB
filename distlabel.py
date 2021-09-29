from geopy.geocoders import GoogleV3

with open('API_KEY.txt','r') as API:
    API_KEY = API.read()

# need to enable Geocoding API in Google Cloud Platform first
geolocator = GoogleV3(API_KEY)
print(type(geolocator))

location = geolocator.geocode('105 BT BATOK CTRL')
print(location.latitude, location.longitude)