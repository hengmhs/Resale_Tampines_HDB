# Tampines HDB 2013 - 2018 Resale Data Tagging

Data obtained from https://data.gov.sg/dataset/resale-flat-prices

Google Geocoding API was used to find the latitude and longitude of HDB flats

Geopy.distance was used to determine the distance between the HDB flats and Tampines MRT

## Legend
In resale2013_2018.xlsx, 
```
    1. distance - the distance of the HDB flat from Tampines MRT
    2. mrt - 1 denotes less than 400m from Tampines MRT and 0 denotes more than 400m from Tampines MRT
```

For the EC4352 Singapore Economy: Practice and Policy module