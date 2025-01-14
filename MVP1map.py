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
    folium.Marker(location=[lat, lon], popup=name, tooltip=name, icon=folium.Icon(color="blue", icon="person-shelter", prefix = "fa")).add_to(MVP1map)

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

# Add custom HTML with dataset name --------------------
# Define the fixed text as an HTML block
dataset_name_html = f"""
<div style="
    position: fixed; 
    bottom: 10px; left: 10px; 
    width: 250px; 
    height: auto; 
    background-color: orange; 
    padding: 10px; 
    border: 2px solid black;
    font-size: 10pt;
    z-index: 1000;">
    Dataset Name: <b>{dataset_name}</b>
</div>
"""

user_input_html = """
    <div style="position: fixed; top: 15%; left: 50%; transform: translate(-50%, -50%); background-color: white; padding: 20px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); border-radius: 8px; z-index: 1000;">
        <h4 style="margin: 0;">Enter your location</h4>
        <input type="text" id="latitude_input" placeholder="Latitude (Ex: 39.5)" style="width: 100%; margin-top: 10px; padding: 5px;"/>
        <input type="text" id="longitude_input" placeholder="Longitude (Ex: -98.35)" style="width: 100%; margin-top: 10px; padding: 5px;"/>
        <br><br>
        <button onclick="alert('Hello, ' + document.getElementById('user_input').value + '!')">Submit</button>
    </div>
    """

# Save the map to an HTML file
MVP1map.save("static/MVP1map.html") #saves the map in an html file for use
with open('static/MVP1map.html', 'r') as file:
    map_html = file.read()
map_html = map_html.replace('</body>', f'{dataset_name_html}</body>') # Insert the custom HTML before the closing </body> tag
map_html = map_html.replace('</body>', f'{user_input_html}</body>')
with open('static/MVP1map.html', 'w') as file: # Save the modified HTML back to the file
    file.write(map_html)


# calculate the pathway
