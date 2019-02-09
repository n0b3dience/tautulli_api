import requests
import json


class Requester:
    """Requester class"""
    def __init__(self, url, payload):
        self.url = url
        self.payload = payload

    def get(self, pprint=False):
        """Send/receive API request"""
        r = requests.get(self.url, params=self.payload)
        if r.status_code == 200:
            if pprint:
                r = json.loads(r.content.decode('utf-8'))
                r = json.dumps(r, sort_keys=True, indent=4)
                return r
            else:
                r = json.loads(r.content.decode('utf-8'))
                return r
        else:
            r.raise_for_status()
