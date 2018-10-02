
import json

from data_salmon.dataset import Dataset
from data_salmon.fields import FieldFactory

from ..input_file_loader import InputFileLoader

class JsonInputFileLoader(InputFileLoader):
    '''
        Loads a json file and transforms it into data_salmon's internal format.
    '''
    @classmethod
    def load(cls, input_stream):
        js_file = json.loads(input_stream.read())

        name = js_file['name']
        fields = js_file['fields']

        dataset = Dataset(name)

        for json_field in fields:
            dataset.append_field(FieldFactory.build_field(
                json_field['type'], json_field['name'], json_field['strategy'],
                json_field['arguments']))

        return dataset