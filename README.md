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
Look at:

def test(...): ...

### 🧠 How it Works

Static rendering via staticmap (uses tile layers)

Interactive rendering via folium (Leaflet under the hood)

Uses OSRM’s /route API to test routes

### 📁 File Overview
```
geo_plotter.py         # Core library
main.py                # Example usage
README.md              # This file
```
