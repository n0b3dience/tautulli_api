from requests.auth import AuthBase


class TautulliApiAuth(AuthBase):
    """Used to add authorization key to request headers"""
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.headers.update(self.get_auth_headers())
        return request

    def get_auth_headers(self):
        """Returns headers with authorization key"""
        return {
            'Content-Type': 'Application/JSON',
            'Authorization': self.api_key
        }
