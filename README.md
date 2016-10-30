# Creezy

Watching polygons on craiglist for new listings meeting criteria.

Consists of

 - Creating a polygon you want places in using latlngs and abusing some tool
 - Writing code to test against these latlngs
 - Getting a firehose of all new craigslist listings to test against
 - Reporting new listings for examination

## Getting the polygon

Hacked streeteasy boundary by setting a breakpoint on line 24774 of [http://cdn-assets-s3.streeteasy.com/assets/app-06ba69c78e19da4252cbfc406f27a0ab.js](the app JS file). Created close_to_bbkqb.json featuring areas in LIC and Astoria close to the climbing gym.

## Testing against the polygon

Use [http://stackoverflow.com/questions/7861196/check-if-a-geopoint-with-latitude-and-longitude-is-within-a-shapefile](this answer), which suggests the `shapely` Python library

## Getting a firehose from craigslist

Use [https://pypi.python.org/pypi/python-craigslist/1.0.0](python-craigslist), which has a convenient API to fetch all listings.

## Reporting

Use my existing mailgun account for now.