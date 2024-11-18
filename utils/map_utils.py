import folium

def create_map(results):
    map_obj = folium.Map(location=[0, 0], zoom_start=2)
    for result in results.get('matches', []):
        lat = result.get('location', {}).get('latitude')
        lon = result.get('location', {}).get('longitude')
        if lat and lon:
            folium.Marker([lat, lon], popup=result.get('ip_str')).add_to(map_obj)
    map_obj.save("shodan_map.html")
    print("Map saved as shodan_map.html")
