import io
import base64

def read_datafile(data):

    if data is not None:
        content_type, content_string = data.split(',')
        decoded = base64.b64decode(content_string)
        datafile = io.StringIO(decoded.decode('utf-8'))

        return datafile