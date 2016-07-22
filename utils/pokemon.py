from datetime import datetime
import time
import json


class Pokemon():
    _meta = None

    def __init__(self, meta):
        self._meta = meta
    
    def get_location(self):
        return {'latitude': self._meta['latitude'], 'longitude': self._meta['longitude']}
    
    def get_id(self):
        return self._meta['pokemon_id']
    
    def get_name(self):
        return self._meta['pokemon_name']
    
    def get_expires_timestamp(self):
        return self._meta['expires']
    
    def get_expires(self):
        return datetime.fromtimestamp(self.get_expires_timestamp())
    
    def __repr__(self):
        location = self.get_location()
        p = dict([('name', self.get_name()), ('lat', location['latitude']), ('long', location['longitude']), ('curtime', time.time()), ('lefttime', self.get_expires_timestamp()), ('exptime', int(self.get_expires_timestamp() - time.time()))])
        with open('data.json', 'a') as f:
            json.dump(p, f, indent=2)
        
        return '%s [%d]: %f, %f, %d seconds left' % (
                                                     self.get_name(),
                                                     self.get_id(),
                                                     location['latitude'],
                                                     location['longitude'],
                                                     int(self.get_expires_timestamp() - time.time())
                                                     )
    