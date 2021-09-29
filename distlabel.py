from geopy.geocoders import GoogleV3
import geopy.distance
from openpyxl import load_workbook, Workbook

with open('API_KEY.txt','r') as API:
    API_KEY = API.read()

# need to enable Geocoding API in Google Cloud Platform first
geolocator = GoogleV3(API_KEY)

# Tampines MRT lat: 1.3533834 long: 103.9451538
tampines_mrt = (1.3533834, 103.9451538)

wb_name = 'resale2013_2018.xlsx'

# Load the Workbook
wb = load_workbook(wb_name)
# Load the Worksheet
sheet = wb['Sheet1']

addr_list = []
# ' ' is padding for index purposes
dist_list = [' ','distance']

# start from 2 to avoid the column headers, range() is one less step than max
for i in range(2, sheet.max_row + 1):
    block = str(sheet.cell(row=i, column=4).value)
    street_name = sheet.cell(row=i, column=5).value
    addr_list.append(block + ' ' + street_name)

addr_list_len = len(addr_list)

for index, address in enumerate(addr_list):
    print(str(index+1)+'/'+str(addr_list_len))
    location = geolocator.geocode(address)
    place = (location.latitude, location.longitude)
    dist =geopy.distance.geodesic(place, tampines_mrt).km
    dist_list.append(dist)

dist_list_len = len(dist_list)

for row in range(1,dist_list_len):
    cell = sheet.cell(column=11, row=row)
    cell.value = dist_list[row]

wb.save(wb_name)