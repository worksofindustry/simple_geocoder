from json import loads
from requests import get
from urllib.parse import quote


def geocode_address(API_KEY='', country='US', locality='', postal_code='', address_line='') -> tuple:
    """geocodes using Google Virtual Earth API
       country: Two letter country code
       address_line: Can contain Street Number + Unit + Street + Street Direction + Suffix
       locality: city or province 
    """
    address_line = quote(address_line)
    url = f"http://dev.virtualearth.net/REST/v1/Locations?countryRegion={country}&adminDistrict=&locality={locality}&postalCode={postal_code}&addressLine={address_line}&key={API_KEY}&output=json"
    
    try:
        api_response = get(url)
    except ConnectionError as e:
        print(e)
        
    if (api_response.status_code == 200):
        data = loads(api_response._content)
        try:
            if data.get('resourceSets')[0].get('resources')[0].get('point').get('coordinates') != None:
                lat, long = data.get('resourceSets')[0].get('resources')[0].get('point').get('coordinates')
        except (IndexError, AttributeError):
            print("Unable to geocode")
        return lat, long
        
if __name__ == '__main__':
    # test example from main
    lat, long = geocode_address(API_KEY="<your-API-KEY-goes-here", locality="Louisville", address_line='401 East Main Street')    
    print("Your coordinates are: ", lat, long)
