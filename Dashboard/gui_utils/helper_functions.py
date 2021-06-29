import io
import base64
from inspect import getmembers, isclass
from models import fit_profiles
import numpy as np



def read_datafile(data):

    if data is not None:
        content_type, content_string = data.split(',')
        decoded = base64.b64decode(content_string)
        datafile = io.StringIO(decoded.decode('utf-8'))

        return datafile



def model_options():
    
    profiles = getmembers(fit_profiles, isclass)
    
    options = []
    for i in range(len(profiles)):
        options.append({'label': profiles[i][0], 'value': profiles[i][0]})
    return options


def model_selection(model_str):

    profiles = getmembers(fit_profiles, isclass)
    
    for i in range(len(profiles)):
   
        if profiles[i][0] == model_str:
            model = profiles[i][1]()

    return model


class Table:
    def __init__(self):

        self.data = []
        self.columns = []

    def update_table(self, fitted_parameters, model):

        n_parameters = len(fitted_parameters)
        
        if len(self.columns) < n_parameters:
            columns = []
            columns.append({'id': 'Model', 'name': "Model"})
            for i in range(n_parameters):
                columns.append({'id': "Parameter " + str(i+1), 'name': "Parameter " + str(i+1)})
            
            self.columns.append(columns)
            self.columns = self.columns[0]

        self.data.append({"Parameter " + str(i+1): np.around(fitted_parameters[i], 2) for i in range(n_parameters)})
        self.data[-1].update({'Model': model})