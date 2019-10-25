from core.auth import GOOGLE_GEOCP_KEY

"""
 -> resolve a latitude/longitude de um endereço;
"""
def format_address(address):
    if address != None:
        return "{street} {number}, {hood}, {city}, {state}".format(
            street=adress.street,
            number=adress.number,
            hood=adress.neighborhood,
            city=adress.city,
            state=adress.state,
            )
    else:
        return None
"""Resolves a valid address to pair of coordinates in SRID 4326
"""
def geocode_address(address):
    geolocator = GoogleV3(api_key=GOOGLE_GEOCP_KEY,
                          user_agent=None,
                          format_string="%s, brazil",
                          timeout=5)
    try:
        location = geolocator.geocode(format_adress_user_select(address))
        return {'latitude': location.latitude,
            'longitude': location.longitude
            }
    except Exception:
        return None
