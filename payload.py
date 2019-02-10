"""Payload class"""


class Payload:
    """API command payload class"""

    def __init__(self, name, **params):
        """Payload constructor"""
        # Command name
        self.name = name
        # Command value
        self.cmd = name
        # Raw base-payload values
        # self._base_payload = {'cmd': self.cmd}
        # Command object *args
        self.params = params
        # Final payload with None values removed
        self.payload = self.update()

    def update(self):
        """Form payload"""
        # Clear payload
        self.clear()
        # Setup local-scope payload base dict
        payload = {'cmd': self.cmd}
        # Add non-None _base_payload keys/vals into payload
        # for key in self._base_payload:
        #     if self._base_payload[key] is not None:
        #         payload[key] = self._base_payload[key]
        #     else:
        #         pass
        # Add non-None _params keys/vals into payload
        for key in self.params:
            if self.params[key] is not None:
                payload[key] = self.params[key]
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
