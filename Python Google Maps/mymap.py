import folium
import pandas 

#in this file I use folium and pandas to load data, and bring up the google map feature
#I also add pinpoints to certian locations, and add pinpoints that represent data cordinates
#that are in the files that I am reading. 
#i create a simple function to change the colors of the pins based on elevation from the data
#I also create a geoJson layer
#I also implement a Choropleth Map
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup= str(el) + " Meters", icon=folium.Icon(color=color_producer(el))))

fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read()))

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")



map.add_child(fg)
map.save("Map1.html")