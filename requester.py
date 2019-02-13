"""
Requester class
"""
import requests
import json


class Requester:
    """Requester class"""

    def __init__(self, url, payload):
        """Requester constructor"""
        self.url = url
        self.payload = payload
        # self.auth = auth

    def get(self, pprint=False):
        """Send/receive API request"""
        r = requests.get(self.url, params=self.payload)
        if r.status_code == 200:
            r = json.loads(r.content.decode('utf-8'))
            if pprint:
                return json.dumps(r, sort_keys=True, indent=4)
            else:
                return r
        else:
            r.raise_for_status()
