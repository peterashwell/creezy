import json

from shapely.geometry import Polygon


def open_fence_file(path):
    with open(path) as contents:
        geojson = json.loads(contents.read())
        points = [
            (p['lat'], p['lng'])
            for p in geojson
        ]
        return Polygon(points)

# Hardcoded geofence paths
CLOSE_TO_BKBB_PATH = 'data/close_to_bbk_qb.json'

# Preprepared shapdely geofences
CloseToBkbQb = open_fence_file(CLOSE_TO_BKBB_PATH)