# py_geo_snippets
Some quick n dirty python snippets useful for geo dev


## 1) 🗺️ geo_plotter.py
A python shorthand to fetch and plot geojson on OSM tiles. Includes testing using the free OSRM API.
Supports both static PNG rendering (no browser required) and interactive HTML map generation.

### ✨ Features
 - 🔵 Plot static PNG maps with OpenStreetMap tiles using staticmap
 - 🌍 Create interactive route maps with folium
 - 📡 Fetch routes using live OSRM API
 - 🖼️ Automatically open generated images/maps in your system’s default viewer/browser

### 📦 Installation
```bash
git clone ...
pip install requests folium staticmap pillow
```

### 🧩 Usage
```python
import geo_plotter
geo_plotter.test() # auto execute a test
# This is how it's actually used:
plot_static_png(geojson, filename="route.png", open_image=True)
plot_interactive_map(center=start, geojson=geojson, filename="route_map.html", open_browser=True)
```

### 🧠 How it Works

Static rendering via staticmap (uses tile layers)

Interactive rendering via folium (Leaflet under the hood)

Uses OSRM’s /route API to test routes

### 📁 File Overview
```
geo_plotter.py         # Core library
README.md              # This file
```
