import math


def calc_distance_between_coords(lat1, lon1, lat2, lon2, kilometers=False):
    """Calculates the great-circle distance between two sets of coordinates.
    
    Uses the Haversine formula - https://en.wikipedia.org/wiki/Haversine_formula
    
    Calculations within the algorithm are in kilometers, but the returned value will 
    be in miles by default, or kilometers if the optional parameter is set.
    """

    earth_radius = 6371
    # We need to work with radians instead of degrees
    lat1_rad = degrees_to_radians(lat1)
    lat2_rad = degrees_to_radians(lat2)
    delta_lat_rad = degrees_to_radians(lat2 - lat1)
    delta_lon_rad = degrees_to_radians(lon2 - lon1)

    a = math.sin(delta_lat_rad / 2) * math.sin(delta_lat_rad / 2) + \
        math.cos(lat1_rad) * math.cos(lat2_rad) * \
        math.sin(delta_lon_rad / 2) * math.sin(delta_lon_rad / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    if kilometers:
        return distance
    else:
        return kilometers_to_miles(distance)


def degrees_to_radians(deg):
    return deg * math.pi / 180

def kilometers_to_miles(kilometers):
    return kilometers / 1.609344
