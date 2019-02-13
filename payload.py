"""
Payload class
"""


class Payload:
    """API command payload class"""

    def __init__(self, **params):
        """Payload constructor"""
        # Command object **kwargs
        self.params = params
        # Final payload with None values removed
        self.payload = self.update()

    def update(self):
        """Form payload"""
        # Setup local-scope payload dict
        payload = {}
        # Add non-None _params keys/vals into payload
        for key in self.params['params']:
            if self.params['params'][key] is not None:
                payload[key] = self.params['params'][key]
            else:
                pass
        return payload

    def clear(self):
        """Clear everything from payload"""
        self.payload.clear()

    def remove_keys(self, *keys):
        """Removes given keys from payload"""
        for key in keys:
            del self.payload[key]
