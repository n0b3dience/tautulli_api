[Tautulli API](https://github.com/n0b3dience/tautulli_api)
============
The Tautulli API module is made to provide a Python 3 wrapper for the 
web API of [Tautulli](https://tautulli.com), the web application for 
monitoring, analytics and notifications for Plex Media Server.

This wrapper was designed to provide an easy to use, one-to-one analogue for 
the Tautulli web API.

_**NOTE:** This is an unofficial work-in-progress and is provided as-is. It has 
not been fully tested. Feel free to report any bugs you may find at the [project's 
Github page](https://github.com/n0b3dience/tautulli_api/issues)._

### Example
#### Tautulli Web API:
```
http://localhost:8181/api/v2?apikey=66198313a092496b8a725867d2223b5f&cmd=get_metadata&rating_key=153037
```
#### Tautulli API Python Wrapper
```
# Construct a Tautulli() object
tautulli = Tautulli(
    host="localhost",
    port=8181,
    apikey="66198313a092496b8a725867d2223b5f",
    schema="http"
)

# Run the command
tautulli.get_metadata(rating_key=153037)
```

### Settings File:
If you'd like to avoid entering the `Tautulli()` parameters (`host=`, 
`port=`, `apikey=`, etc.) each time you instantiate a `Tautulli()` object, you 
can fill in the values of `host`, `port`, `api_key` and `schema` in the 
[settings.ini](./settings.ini) file located in the root of the project 
directory.

### Tautulli Web API:
See the [API documentation](./API.md) for details.


