import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

key = "Your Key"  # Replace with your valid API key

number = input("Please enter your phone number (with or without +91): ")

# Use 'IN' as the default region for Indian numbers
new_number = phonenumbers.parse(number, "IN")

# Get location and carrier
location = geocoder.description_for_number(new_number, "en")
print("Location:", location)

service_name = carrier.name_for_number(new_number, "en")
print("Carrier:", service_name)

# Geocode the location
geocoder_opencage = OpenCageGeocode(key)
query = str(location)
result = geocoder_opencage.geocode(query)

# Ensure there's at least one result
if result:
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    print("Latitude:", lat)
    print("Longitude:", lng)

    # Generate map
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)
    my_map.save("location.html")

    print("Location tracking completed.")
    print("Map saved as 'location.html'.")
else:
    print("Could not geocode the location.")
v
