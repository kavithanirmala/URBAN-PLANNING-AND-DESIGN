import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

# Sample zones: residential, commercial, green space
zones = {
    "Residential": Polygon([(1, 1), (5, 1), (5, 5), (1, 5)]),
    "Commercial": Polygon([(6, 1), (10, 1), (10, 5), (6, 5)]),
    "Green_Space": Polygon([(3, 6), (7, 6), (7, 9), (3, 9)])
}

# Create GeoDataFrame
zone_data = gpd.GeoDataFrame({
    'Zone_Type': list(zones.keys()),
    'geometry': list(zones.values())
})

# Buffer around residential zone (1 km radius) to check nearby green areas
residential_zone = zone_data[zone_data['Zone_Type'] == 'Residential'].geometry.iloc[0]
buffer_zone = residential_zone.buffer(1.0)

# Check if green space intersects the buffer
green_space = zone_data[zone_data['Zone_Type'] == 'Green_Space'].geometry.iloc[0]
is_nearby = buffer_zone.intersects(green_space)

# Output result
print(f"Is green space within 1km of residential area? {'Yes' if is_nearby else 'No'}")
