# Tampines HDB 2013 - 2018 Resale Data Tagging

Data obtained from https://data.gov.sg/dataset/resale-flat-prices

Google Geocoding API was used to find the latitude and longitude of HDB flats

Geopy.distance was used to determine the distance between the HDB flats and Tampines MRT

## Legend
In resale2013_2018.xlsx, 
```
    1. lat - the latitude of the HDB flat
    2. long - the longitude of the HDB flat
    3. dist_tampines - the distance between the HDB flat and Tampines MRT
    4. dist_east - the distance between the HDB flat and Tampines East MRT
    5. dist_west - the distance between the HDB flat and Tampines West MRT
    6. tampines_mrt - 1 denotes less than 400m from Tampines MRT and 0 denotes more than 400m from Tampines MRT
    7. east_mrt - 1 denotes less than 400m from Tampines East MRT and 0 denotes more than 400m from Tampines East MRT
    8. west_mrt - 1 denotes less than 400m from Tampines West MRT and 0 denotes more than 400m from Tampines West MRT
```

For the EC4352 Singapore Economy: Practice and Policy module