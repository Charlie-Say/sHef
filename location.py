"""
This program will use a google API to find current location and date to compare
with a table of seasons. We can take this information and tell the user
what is in season in their location.


------------ psuedocode --------------------


"""

import geocoder


def location():
    # this is current latitude/longitude
    g = geocoder.ip('me')
    print(g.address)
    return g.address

# testing
location()