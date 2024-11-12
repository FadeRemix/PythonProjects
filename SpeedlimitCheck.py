import requests

# Replace with your actual latitude and longitude
latitude = 28.471634748904176  # Example: New York City latitude
longitude = -80.78818411147849  # Example: New York City longitude

# Create the Overpass API query
query = f"""
[out:json];
(
  way["maxspeed"](around: 50, {latitude}, {longitude});
);
out body;
>;
out skel qt;
"""

# The Overpass API URL
url = "http://overpass-api.de/api/interpreter"

# Print the query for debugging
#print("Query:", query)

# Send the request with query as a parameter
response = requests.get(url, params={'data': query})

# Check the response status
if response.status_code == 200:
    data = response.json()
    
    # Check if there are any elements in the response
    if 'elements' in data and data['elements']:
        # Print only the max speed of the first matching element
        for element in data['elements']:
            if 'tags' in element and 'maxspeed' in element['tags']:
                print(f"Max speed: {element['tags']['maxspeed']}")
                break  # Stop after the first match
        else:
            print("No max speed found for this location.")
    else:
        print("No elements found in response.")
else:
    print("Error:", response.status_code, response.text)
