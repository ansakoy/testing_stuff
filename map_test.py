import folium

my_map = folium.Map(location=[55.668006, 37.556893],
        zoom_start=6, tiles='Mapbox Bright')

#dd elements to the map
#Get help om this method
#help(folium.Marker)
#y_map.add_child(folium.Marker(location=[55.7, 37.5], popup='This is a marker', icon=folium.Icon(color='green')))

feature_group = folium.FeatureGroup(name='My Map')

#feature_group.add_child(folium.Marker(location=[55.7, 37.5], popup='This is a marker', icon=folium.Icon(color='green')))
my_map.add_child(feature_group)

my_coords = [[55.6, 37.5], [57.6, 35.3]]
for coord in my_coords:
    print(coord)
    feature_group.add_child(folium.Marker(location=coord, popup='This is a marker', icon=folium.Icon(color='green')))

my_map.save('map1.html')
