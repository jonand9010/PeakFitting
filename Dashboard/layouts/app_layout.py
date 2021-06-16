
import dash_html_components as html
import dash_core_components as dcc
from inspect import getmembers, isclass

def model_options():
    from models import fit_profiles
    profiles = getmembers(fit_profiles, isclass)
    
    options = []
    for i in range(len(profiles)):
        options.append({'label': profiles[i][0], 'value': profiles[i][0]})
    return options


def App_Layout():
    layout = html.Div([
        html.Div([
        html.H1('Peak fitting'),
        dcc.Upload(id = 'data-import', children = html.Div(['Drag and Drop or ', html.A('Select File')]),
                    style = {'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px',
            'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}, multiple = False),

        dcc.Dropdown(id = 'Model-selection', options = model_options(), 
                placeholder = 'Choose a model')
                    
            ]),
        

        dcc.Graph(id = 'Raw-data-plot'),


        dcc.Graph(id = 'Model-fit-plot'),

        dcc.Graph(id = 'Residuals-plot')

        ])

    return layout

