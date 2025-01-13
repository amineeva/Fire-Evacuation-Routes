import folium
from folium.plugins import MarkerCluster
from folium.features import DivIcon
import pandas as pd
import webbrowser
import tempfile

#want to center around the middle of america
middle_coords = [39.5, -98.35]

#Create the map
MVP1map = folium.Map(location = middle_coords, zoom_start = 5)

# user_lat = input("Enter latitude: ")
# user_long = input("Enter longitude: ")
# user_coords = [user_lat, user_long]  
user_coords = [47.36, -122.20]

print("Your coordinates are: " + str(user_coords[0]) + ", " + str(user_coords[1]))

#putting down pins (1: drop and 2: coordinates)
folium.Marker(location=user_coords, popup="User Location", icon=folium.Icon(color="purple")).add_to(MVP1map)

#Palisades Evacuation Sites and Shelters Dictionary -------------------
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
    folium.Marker(location=[lat, lon], popup=name, tooltip=name, icon=folium.Icon(color="blue", icon="fire", prefix = "fa")).add_to(MVP1map)

# DATASET ---------------------------------------------------------------
USA_url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/8a9f5ecbad092d21416c6105e7313d55/VIIRS_SNPP_NRT/-125,24,-66,49/1/2025-01-10'
df_USA = pd.read_csv(USA_url)
df_USA
# Split the URL and extract the parts
parts = USA_url.split('/')

# Extract the necessary parts
sensor = parts[7]  # VIIRS_SNPP_NRT
date = parts[10]   # 2025-01-10
dataset_name = str(sensor) + " - " + str(date) #"VIIRS SNPP NRT - 01/10/25"

for index, row in df_USA.iterrows():
    # Define rectangle bounds (a small box around the latitude/longitude)
    bounds = [[row['latitude'] - 0.01, row['longitude'] - 0.01], [row['latitude'] + 0.01, row['longitude'] + 0.01]]
    folium.Rectangle(bounds=bounds, color="red",  fill=True, fill_color="red",fill_opacity=0.5, tooltip="Fire").add_to(MVP1map)

# Add a marker with the popup containing the textbox --------------------
folium.map.Marker(
    [30, -120],
    icon=DivIcon(
        icon_size=(250,36),
        icon_anchor=(0,0),
        html=f'<b><span style="background-color: orange; padding: 5px; font-size: 16pt;">{dataset_name}</span></b>',
        )
    ).add_to(MVP1map)




# calculate the pathway

# Very last thing!! This is the final map
MVP1map.save("MVP1map.html") #saves the map in an html file for use