import gmplot
from openpyxl import load_workbook, Workbook

wb_name = 'resale2013_2018.xlsx'

# Load the Workbook
wb = load_workbook(wb_name)
# Load the Worksheet
sheet = wb['Sheet1']


with open('API_KEY.txt','r') as API:
    API_KEY = API.read()

gmap = gmplot.GoogleMapPlotter(1.3533834, 103.9451538, 14, apikey=API_KEY)

coord_list = []

# start from 2 to avoid the column headers, range() is one less step than max
# get coordinates of each place
for i in range(2, sheet.max_row + 1):
    lat = sheet.cell(row=i, column=11).value
    longitude = sheet.cell(row=i, column=12).value
    coord = (lat, longitude)
    coord_list.append(coord)

# removes duplicates
coord_set = set(coord_list)

# convert set back to list
coord_list = list(coord_set)

'''
for coord in coord_list:
    gmap.scatter(coord[0], coord[1], color='blue')
'''

gmap.scatter(1.3533834,103.9451538)

gmap.draw('map.html')