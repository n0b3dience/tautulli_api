"""
Validator Class
"""
import os
import json
from jsonschema import validate, ValidationError, SchemaError, RefResolver


class Validator:
    """JSON Schema validator class"""

    def __init__(self, payload):
        """Validator constructor"""
        self.payload = payload
        self.name = self.payload['cmd']
        self.schema_file = self._get_schema_file_name()
        # self.base_pl_keys = ['apikey', 'cmd', 'out_type', 'callback', 'debug']
        self._schema_dir = os.path.abspath('schemas')
        # Ref resolver for schema files
        self._resolver = RefResolver(
            'file:///{}/'.format(self._schema_dir), None)

    def _get_schema_file_name(self):
        """Return schema file name"""
        if self.payload.keys() in (
            'apikey', 'cmd', 'out_type', 'callback', 'debug'
        ):
            return './schemas/payload.json'
        else:
            return './schemas/{}.json'.format(self.name)

    def validate(self):
        """Validate payload with JSON Schema"""
        try:
            with open(self.schema_file, 'r') as schema_file:
                print('Schema:  ::: {} :::  opened...'.format(self.schema_file))
                schema = json.load(schema_file)
                validate(instance=self.payload, schema=schema,
                         resolver=self._resolver)
        except ValidationError as e:
            print(':::VALIDATION ERROR:::\n{0} : {1}\n{2}'.format(
                e.validator.__str__(), e.parent, e.message))
            print(e)
        except SchemaError as e:
            print(':::SCHEMA ERROR:::\n{0} : {1}\n{2}'.format(
                e.cause, e.validator_value, e.message))
