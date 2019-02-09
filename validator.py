import os
import json
from jsonschema import validate, ValidationError, SchemaError, RefResolver


class Validator:
    """JSON Schema validator class"""
    def __init__(self, payload):
        self.payload = payload
        self.name = self.payload['cmd']
        self.schema_file = self._get_schema_file_name()
        self.base_pl_keys = ('apikey', 'cmd', 'out_type', 'callback', 'debug')
        self._schema_dir = os.path.abspath('schemas')
        # Ref resolver for schema files
        self._resolver = RefResolver(
            'file:///{}/'.format(self._schema_dir), None)

    def _get_schema_file_name(self):
        """Return schema file name"""
        if self.payload.keys() in self.base_pl_keys:
            return 'payload.json'
        else:
            return '{}.json'.format(self.name)

    def validate(self):
        """Validate payload with JSON Schema"""
        try:
            with open(self.schema_file, 'r') as schema_file:
                schema = json.load(schema_file)
                validate(instance=self.payload, schema=schema,
                         resolver=self._resolver)

        except ValidationError as e:
            print(e.message)

        except SchemaError as e:
            print(e.message)
