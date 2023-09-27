import requests

API_KEY = 'my actual Google API key'

address = 'Sanowara R/A, Chattogram'

api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

params = {
    'address': address,
    'key': API_KEY,
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    if data['status'] == 'OK':
        # Extract latitude and longitude from the response
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        print(f'Address: {address}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print(f'Geocoding failed. Status: {data["status"]}')
else:
    print(f'Request failed. Status Code: {response.status_code}')
