import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser
import tempfile

#want to center around the middle of america
middle_coords = [39.5, -98.35]

#Create the map
MVP1map = folium.Map(location = middle_coords, zoom_start = 4)

# user_lat = input("Enter latitude: ")
# user_long = input("Enter longitude: ")
# user_coords = [user_lat, user_long]  
user_coords = [47.36, -122.20]

print("Your coordinates are: " + str(user_coords[0]) + ", " + str(user_coords[1]))

#putting down pins (1: drop and 2: coordinates)
folium.Marker(location=user_coords, popup="User Location").add_to(MVP1map)

#Palisades Evacuation Sites and Shelters Dictionary
evac_sites = {
    "Calvary Community Church": (33.8438089, -118.29581),
    "Ritchie_Valens_Recreation_Center": (34.16041, -118.26169),
    "Pasadena Civic Center": (34.143383, -118.144243),
    "Pan Pacific Recreational Center": (34.431656, -118.21163188),
    "Westwood Recreation Center": (34.05332287438061, -118.4484818326542),
    "Stoner Recreation Center": (34.03863740339764, -118.45347907498306),
    "Pomona Fairplex": (34.081099137102655, -117.76651258847353)
}
# Add markers for each place
for name, coords in evac_sites.items():
    lat, lon = coords
    folium.Marker(location=[lat, lon], popup=name, tooltip=name, icon=folium.Icon(color="blue", icon="person-shelter", prefix = "fa")).add_to(MVP1map)


# calculate the pathway

#





# Very last thing!! This is the final map
MVP1map.save("MVP1map.html") #saves the map in an html file for use