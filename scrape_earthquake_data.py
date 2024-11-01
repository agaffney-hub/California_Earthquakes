import requests
import pandas as pd
from datetime import datetime, timedelta

def scrape_earthquake_data():
    # Calculate the time one week ago
    one_week_ago = datetime.now() - timedelta(days=7)
    start_time = one_week_ago.strftime('%Y-%m-%d')

    # URL for fetching earthquake data from the past week
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_time}&endtime={datetime.now().strftime('%Y-%m-%d')}"

    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return

    data = response.json()

    # Check if features are present
    if 'features' not in data:
        print("No earthquake data found.")
        return

    earthquakes = []
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        
        earthquakes.append({
            'magnitude': properties['mag'],
            'location': properties['place'],
            'time': datetime.fromtimestamp(properties['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
            'latitude': geometry['coordinates'][1],
            'longitude': geometry['coordinates'][0]
        })

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(earthquakes)
    df.to_csv('data/earthquake_data.csv', index=False)

if __name__ == "__main__":
    scrape_earthquake_data()
