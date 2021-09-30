import gmplot
from openpyxl import load_workbook, Workbook

wb_name = 'resale2013_2018.xlsx'

# Load the Workbook
wb = load_workbook(wb_name)
# Load the Worksheet
sheet = wb['Sheet1']

with open('API_KEY.txt','r') as API:
    API_KEY = API.read()

gmap = gmplot.GoogleMapPlotter(1.3533834, 103.9451538, 15, apikey=API_KEY)

coord_list = []
# list of hdbs near tampines MRT
tamp_list = []

# start from 2 to avoid the column headers, range() is one less step than max
# get coordinates of each place
for i in range(2, sheet.max_row + 1):
    lat = sheet.cell(row=i, column=11).value
    longitude = sheet.cell(row=i, column=12).value
    coord = (lat, longitude)
    # get value of tampines_mrt, east_mrt, west_mrt
    tampines_mrt = sheet.cell(row=i,column=16).value
    east_mrt = sheet.cell(row=i,column=17).value
    west_mrt = sheet.cell(row=i,column=18).value
    # check if tampines_mrt = 1
    if tampines_mrt:
        tamp_list.append(coord)
    # check if coord is near east_mrt or west_mrt
    elif not east_mrt and not west_mrt :
        coord_list.append(coord)

# removes duplicates
tamp_set = set(tamp_list)
# convert set back to list
tamp_list = list(tamp_set) 

tamp_list_lat = []
tamp_list_long = []

for coord in tamp_list:
    tamp_list_lat.append(coord[0])
    tamp_list_long.append(coord[1])

# removes duplicates
coord_set = set(coord_list)
# convert set back to list
coord_list = list(coord_set)

coord_list_lat = []
coord_list_long = []

for coord in coord_list:
    coord_list_lat.append(coord[0])
    coord_list_long.append(coord[1])

# scatter takes a list of lats and longs
gmap.scatter(tamp_list_lat,tamp_list_long,size=8,color='red',marker=False,alpha=1)
gmap.scatter(coord_list_lat, coord_list_long,size=8,color='blue',marker=False)

gmap.circle(1.3533834, 103.9451538,400,face_alpha=0,edge_color='red')
gmap.circle(1.3558290924997582, 103.95520090009265,400,face_alpha=0,edge_color='blue')
gmap.circle(1.345808393511592, 103.9382382867281,400,face_alpha=0,edge_color='blue')
gmap.circle(1.3433117614470864, 103.95364307656335,400,face_alpha=0,edge_color='blue')
gmap.circle(1.3418146392239008, 103.96183240725058,400,face_alpha=0,edge_color='blue')
gmap.draw('visualisation.html')