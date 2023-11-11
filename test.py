import airportsdata
airports = airportsdata.load()
data = airports['KJFK']

latitude = data['lat']
longitude = data['lon']

print(longitude)
