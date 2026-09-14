# 🛰️ ASAT-2: Satellite GIS & Eucalyptus Detection Agent

**ASAT-2** is an interactive web platform and automated conversational GIS frontend designed to fetch real Earth Observation data (Sentinel-2 L2A via open STAC) and identify spectral signatures of **Eucalyptus plantations and forests** (e.g. *Eucalyptus globulus*, *Eucalyptus grandis*).

---

## 🌟 Key Features

1. **Automated Conversational GIS Agent**:
   - Natural language map navigation and automated analysis.
   - Command the AI: *"Scan current map for Eucalyptus plantations"*, *"Fly to Eucalyptus forests in Portugal"*, *"Explain how Eucalyptus is separated from Pine using SWIR/NDRE"*.
   - Automated polygon demarcations and canopy area calculations.

2. **Multi-Spectral Satellite Analysis**:
   - **NDVI (Normalized Difference Vegetation Index)**: `(B08 - B04) / (B08 + B04)` (detects high photosynthetic vigor).
   - **NDRE (Red Edge Chlorophyll Index)**: `(B08 - B05) / (B08 + B05)` (sensitive to dense eucalyptus canopy without early saturation).
   - **MSI / Water Absorption (SWIR)**: `B11 / B08` (leverages distinct pendulous leaf moisture reflection characteristics to differentiate from conifers and deciduous oak).

3. **Live STAC Integration**:
   - Queries open **Sentinel-2 L2A STAC APIs** (AWS Element84 / Microsoft Planetary Computer) for cloud-free satellite acquisitions.
   - Displays scene acquisition timestamps, cloud cover percentages, and multi-spectral band assets.

4. **Global Eucalyptus Hotspot Presets**:
   - 🌲 **Portugal (Centro / Viseu)**: Intensive pulp production stands.
   - 🌳 **Brazil (Minas Gerais / Belo Oriente)**: High-yield clonal forestry.
   - 🐨 **Australia (Blue Mountains, NSW)**: Native eucalyptus forest ecosystems with natural terpene haze.
   - 🌿 **California (Berkeley Hills / Tilden)**: Historic Blue Gum stands.
   - 🍃 **India (Nilgiris / Ooty)**: High-altitude plantation landscape.

5. **Interactive Controls & Visualization**:
   - Dynamic sensitivity / probability threshold slider (`0.40 - 0.90`).
   - Draw custom bounding boxes directly on the satellite map using Leaflet Draw.
   - Live spectral reflectance curve comparison chart (Eucalyptus vs. Pinus vs. Quercus).

---

## 🚀 Quickstart

### Option 1: Direct Browser Access
Because ASAT-2 is built with modern vanilla JavaScript and client-side STAC fetching, you can open `index.html` directly in any web browser without any prerequisites:
```bash
open index.html  # On macOS
xdg-open index.html  # On Linux
```

### Option 2: Run with Python
To run the included Python GIS API backend and local server:
```bash
python3 server.py
```
Then visit **`http://localhost:8080`** in your browser.

---

## 📁 Repository Structure
```
asat2/
├── index.html            # Main interactive GIS frontend & Leaflet map UI
├── app.js                # Map controllers, STAC API queries & Chatbot logic
├── detect_eucalyptus.py  # Production CLI Sentinel-2 Multi-Spectral Classifier
├── gis_engine.py         # Python spectral analysis & STAC API processing algorithms
├── server.py             # Lightweight Python API gateway & static server
└── README.md             # Comprehensive project documentation
```

---

## 🔬 Scientific Classification & Ground Truth

### 1. Ground Truth Forestry Inventory Cadastre
ASAT-2 displays **official surveyed forestry inventory boundaries** with real cadastral metadata, including:
- **Portugal (Viseu/Águeda)**: ICNF National Forest Inventory & Altri/Navigator FSC concessions (*E. globulus*).
- **India (Kolar/Bangalore)**: Karnataka Forest Department agroforestry registry (*E. tereticornis*).
- **Brazil (Minas Gerais)**: MapBiomas Silvicultura & Cenibra clonal silviculture (*E. grandis x urophylla*).

### 2. Multi-Spectral Pixel Inspector
Click the **🎯 Inspect** tool in the Layers panel and tap anywhere on Earth:
- Audits multi-spectral surface reflectance across Red (B04), Red-Edge (B05), NIR (B08), and SWIR (B11).
- Checks point against verified cadastral registries.
- Queries live Sentinel-2 STAC metadata for the exact granule and sensing date.

### 3. CLI Pixel Classifier (`detect_eucalyptus.py`)
Run automated multi-spectral detection from the terminal:
```bash
# Run automated self-tests
python3 detect_eucalyptus.py --test

# Scan custom bounding box and export GeoJSON
python3 detect_eucalyptus.py --bbox -8.0 40.6 -7.8 40.8 --threshold 0.68 --output eucalyptus.geojson
```

---

## 🔬 Eucalyptus Spectral Identification Method

| Band | Wavelength | Characteristic for Eucalyptus |
|------|------------|-------------------------------|
| **B04 (Red)** | 665 nm | Strong chlorophyll-a absorption |
| **B05 (Red Edge 1)**| 705 nm | Steep rise indicating high foliar nitrogen/chlorophyll |
| **B08 (NIR)** | 842 nm | High canopy scattering peak (~48-54% reflectance) |
| **B11 (SWIR 1)** | 1610 nm | Differentiates broadleaf vertical leaves from needleleaf conifers |
