import requests
from staticmap import StaticMap, Line
import folium
import os
import subprocess
import sys

def plot_static_png(geojson, filename="route.png", open_image=False):
    """Generate and optionally open a static PNG route map."""

    m = StaticMap(600, 400, url_template='http://a.tile.openstreetmap.org/{z}/{x}/{y}.png')
    m.add_line(Line(geojson, 'blue', 3))
    image = m.render()
    image.save(filename)

    if open_image:
        if sys.platform.startswith('darwin'):
            subprocess.run(['open', filename])
        elif os.name == 'nt':
            subprocess.run(['start', filename], shell=True)
        elif os.name == 'posix':
            subprocess.run(['xdg-open', filename])


def plot_interactive_map(center, geojson, filename="route_map.html", open_browser=False):
    """Generate and optionally open an interactive HTML map with GeoJSON."""
  
    m = folium.Map(location=center, zoom_start=14)
    folium.GeoJson(geojson, name="route").add_to(m)
    m.save(filename)

    if open_browser:
        if sys.platform.startswith('darwin'):
            subprocess.run(['open', filename])
        elif os.name == 'nt':
            subprocess.run(['start', filename], shell=True)
        elif os.name == 'posix':
            subprocess.run(['xdg-open', filename])

# used for testing only:
def test(base_url = "http://router.project-osrm.org/route/v1/driving/"):
    """Fetch a route from the OSRM API."""
    start = (52.517037, 13.388860)  # (lat, lon)
    end = (52.529407, 13.397634)
    overview='full'
    geometry='geojson'
    coords = f"{start[1]},{start[0]};{end[1]},{end[0]}"
    params = {"overview": overview, "geometries": geometry}
    response = requests.get(base_url + coords, params=params)
    response.raise_for_status()
    route = response.json()['routes'][0]['geometry']
    geojson = route['coordinates']
    # This is how it's used:
    plot_static_png(geojson, filename="route.png", open_image=True)
    plot_interactive_map(center=start, geojson=geojson, filename="route_map.html", open_browser=True)
