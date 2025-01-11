import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser
import tempfile

#want to center around the middle of america
middle_coords = [39.5, -98.35]

#Create the map
MVP1map = folium.Map(location = middle_coords, zoom_start = 4)

user_lat = input("Enter latitude: ")
user_long = input("Enter longitude: ")
user_coords = [user_lat, user_long]  #user_coords = [47.36, -122.20]

print("Your coordinates are: " + str(user_coords[0]) + ", " + str(user_coords[1]))

#putting down pins (1: drop and 2: coordinates)
folium.Marker(location=user_coords, popup="User Location").add_to(MVP1map)



MVP1map.save("MVP1map.html") #saves the map in an html file for use