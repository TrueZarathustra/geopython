import folium
from openrouteservice import client


def find_pois(location, distance_range, poi_category):
    '''
    Args:
        location (list): coordinates of initial location (lat, lon)
        distance_range (int): distance from initial locaton
        poi_category (dict): poi categories according to https://github.com/GIScience/openrouteservice-docs#places-response

    Args example:
        location = [55.998976, 37.219673]
        distance_range = 1000
        poi_category = {'atm': 191}

    Returns:
        str: containing html-code with a map and poi-markers on it 
    '''
    api_key = '5b3ce3597851110001cf62482ccff5e54ea24de79d108a5cb78f7d78' 
    location = (location)
    clnt = client.Client(key=api_key)
    map_1 = folium.Map(tiles='Stamen Toner', location=(location), zoom_start=15)
    params_iso = {'range_type': 'distance',
                  'range': [distance_range],
                  }
    params_iso['locations'] = [list(reversed(location))]
    my_region = dict()
    my_region['iso'] = clnt.isochrones(**params_iso)
    folium.features.GeoJson(my_region['iso']).add_to(map_1)

    params_poi = {'request': 'pois',
                  'sortby': 'distance'}

    my_region['categories'] = dict()
    params_poi['geojson'] = my_region['iso']['features'][0]['geometry']

    # for now, frontend supports only 1 category per request, but backend is ready to work with a multiply categories
    for typ, category in poi_category.items():
        params_poi['filter_category_ids'] = category
        my_region['categories'][typ] = dict()
        my_region['categories'][typ]['geojson'] = clnt.places(**params_poi)[0]['features']
    
    poi_coords = {}

    for cat, pois in my_region['categories'].items():
        for poi in pois['geojson']:
            if cat not in poi_coords:
                poi_coords[cat] = []
            poi_coords[cat].append(poi['geometry']['coordinates'])

    for cat, pois in poi_coords.items():
        for poi in pois:
            folium.map.Marker(list(reversed(poi)),
                                          icon=folium.Icon(color='white',
                                                           icon_color='#1a1aff',
                                                           icon='angle-down',
                                                           prefix='fa'
                                                          )
                                         ).add_to(map_1)
    return map_1._repr_html_()