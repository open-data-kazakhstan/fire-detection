# Earth Engine Mosaic Generator
# Fire Detection

## Overview
The project analyzes MOD14A1 V6.1 data, providing composite daily fire masks at a 1 km resolution based on MODIS emissions. The fire detection strategy combines absolute detection (detecting when the fire's strength is sufficient) and relative detection concerning its background (considering surface temperature variability and sunlight reflection). The information is utilized for monitoring the spatial and temporal distribution of fires in diverse ecosystems, detecting changes in fire spread, and identifying new fire boundaries, forest fires, and variations in fire frequency or relative strength.

## Requirements
- Earth Engine Python API
- geemap
- imageio
- Pillow

## Installation

Clone the repository
```shell
$ git clone https://github.com/open-data-kazakhstan/fire-detection.git
```

Requires Python 3.12.0 

Package for interactive geospatial analysis and visualization using Google Earth Engine.
```
pip install geemap
```

Library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.
```
pip install imageo
```

Python image library
```
pip install Pillow
```

## Code Description

### Earth Engine Initialization
Ensure authentication and initialization of the Earth Engine Python API:

```python
import ee
import geemap

# Authentication and Earth Engine initialization
ee.Initialize()
```

## Generating Yearly Mosaics
Load Kazakhstan boundaries:
```python
kazakhstan = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017') \
    .filter(ee.Filter.eq('country_na', 'Kazakhstan'))
```

Define functions for obtaining image IDs and generating mosaics:
```python
def get_image_ids(collection):
    image_ids = collection.aggregate_array('system:index')
    return image_ids

def generate_mosaic(year):
    # ... (see code for more details)
```
Create mosaics for each year:
```python
# Iterating over years and generating mosaics
for year in range(2000, 2022):
    generate_mosaic(year)
```
## Scripts
* `main.py` - main program script
* `animation.py` - script for video animation

## Data
Satellite data taken from https://developers.google.com/earth-engine/datasets.
Data in the form of PNG images for animation is stored in the “data” folder.

## Map Visualization
Display mosaics on an interactive map using geemap:
```# Creating a map
Map = geemap.Map()
Map.centerObject(kazakhstan, 4)
Map.setCenter(65.5, 47, 4)  # Adjusting the map center
Map.addLayer(kazakhstan, {}, 'Kazakhstan')  # Adding Kazakhstan boundaries to the map

# Iterating over years and adding mosaic layers to the map
for year in range(2000, 2023):
    generate_mosaic(year)

Map.addLayerControl()  # Adding a layer control element to the map
Map
```

## Creating Seasonal Animations
1. Change the font path, size and position.
2. Select the appropriate images (specify the path to the images).
3. Run the script to create the animation.
4. Save the animation in MP4 format.

## Data Source
MOD14A1.061: Terra Thermal Anomalies & Fire Daily Global.

## Additional Information
The script utilizes MODIS Land Surface Temperature data to generate yearly mosaics.
Mosaics are displayed on an interactive map for visual exploration.
You can customize the script to choose specific images for map display or comment out the block for saving mosaic images to speed up loading.

## Credits
Original code by [Edward_Schiller]

MODIS MOD14A1.061 data source: [[Google EE] https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD14A1]

## License
This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].
[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/