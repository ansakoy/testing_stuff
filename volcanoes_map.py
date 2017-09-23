import folium
import pandas
import json

my_map = folium.Map(location=[40.146036, -111.096217], zoom_start=6, tiles='Mapbox Bright')

fgroup_v = folium.FeatureGroup(name='Volcanoes')

fgroup_p = folium.FeatureGroup(name='Population')

volcanoes = pandas.read_csv('Volcanoes_USA.txt')
#print(volcanoes.columns)

lons = list(volcanoes.LON)
lats = list(volcanoes.LAT)
elevs = list(volcanoes.ELEV)

def pick_color(val):
    if val < 1000:
        return 'green'
    elif 1000 <= val < 3000:
        return 'orange'
    else:
        return 'red'

for lat, lon, elev in zip(lats, lons, elevs):
    #fgroup.add_child(folium.Marker(location=[lat, lon], popup=str(elev) + ' m', icon=folium.Icon(icon='circle-o', color=pick_color(elev))))

    fgroup_v.add_child(folium.CircleMarker(location=[lat, lon],
        radius=6, 
        popup=str(elev) + ' m', 
        fill_opacity=.8, 
        fill=True, 
        color=pick_color(elev)))

data = open('web_map/world.json', 'r', encoding='utf-8-sig')

fgroup_p.add_child(folium.GeoJson(data=data.read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
    else 'red'}))

my_map.add_child(fgroup_v)
my_map.add_child(fgroup_p)

my_map.add_child(folium.LayerControl())
data.close()

#with open('web_map/world.json', 'r', encoding='utf-8-sig') as handler:
  #  data = json.load(handler)
 #   print(len(data))
#    print(type(data))

my_map.save('volcanoes.html')
