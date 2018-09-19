
import json

from data_salmon.dataset import Dataset
from data_salmon.fields import Field
from data_salmon.fields import IntegerField
from data_salmon.fields import StringField

from ..input_file_loader import InputFileLoader

class JsonInputFileLoader(InputFileLoader):
    '''
        Loads a json file and transforms it into a format data_salmon
        understands
    '''
    def __init__(self):
        pass

    @classmethod
    def build_field(cls, json_field):
        if 'type' not in json_field:
            raise ValueError('Field {} missing type.'.format(json_field))

        _type = json_field['type']
        del json_field['type']

        if 'name' not in json_field:
            raise ValueError('Field {} missing name.'.format(json_field))

        name = json_field['name']
        del json_field['name']

        registered_types = list(StringField.supported_types) + \
                           list(IntegerField.supported_types)

        if _type not in registered_types:
            raise ValueError('Unknown type found: {}. Valid types: {}.'.format(
                _type, registered_types))

        if _type == 'string':
            return StringField(name, **json_field)
        elif _type in IntegerField.supported_types:
            signed = False

            if _type.startswith('int'):
                signed = True
                bit_length = int(_type[3:])
            else:
                signed = False
                bit_length = int(_type[4:])

            return IntegerField(name, **json_field, signed=signed,
                                bit_length=bit_length)
        else:
            return Field(name, **json_field)

    @classmethod
    def load(cls, input_file_path):
        js_file = dict()

        with open(input_file_path, 'r') as f:
            js_file = json.load(f)

        name = js_file['name']
        fields = js_file['fields']

        dataset = Dataset(name)

        for json_field in fields:
            dataset.append_field(JsonInputFileLoader.build_field(json_field))

        return dataset