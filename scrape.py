from craigslist import CraigslistHousing
from shapely.geometry import Point

from fences import CloseToBkbQb

cl_h = CraigslistHousing(site='newyork', area='que', category='aap',
                         filters={'min_price': 1200, 'max_price': 2500})

for apt in cl_h.get_results(sort_by='newest', geotagged=True):
    print(apt.keys())
    if 'geotag' in apt and apt['geotag'] is not None:
        apt_point = Point(*apt['geotag'])
        print("Apartment Point", apt_point)
        if CloseToBkbQb.contains(apt_point):
            print(apt)