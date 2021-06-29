
import dash_html_components as html
import dash_core_components as dcc
import dash_table
from inspect import getmembers, isclass
import pandas as pd
import numpy as np
from gui_utils.helper_functions import model_options



df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
def App_Layout():
    layout = html.Div([
        html.Div([
        html.H1('Peak fitting'),
        dcc.Upload(id = 'data-import', children = html.Div(['Drag and Drop or ', html.A('Select File')]),
                    style = {'width': '90%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px',
            'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}, multiple = False),

        dcc.Dropdown(id = 'Model-selection', options = model_options(), 
                placeholder = 'Choose a model', style = {'width': '35%', 'margin': '10px'})
                    
            ]),
        
        
        dcc.Graph(id = 'Raw-data-plot',style = {'width': '95%'}),


        dcc.Graph(id = 'Model-fit-plot',style = {'width': '95%'}),

        dcc.Graph(id = 'Residuals-plot',style = {'width': '95%'}),

        html.Div([
            html.H2('Fit results'),
            dash_table.DataTable(id = 'Fit-Results', data = [])
            
        ], style = {'width': '90%'}),

        html.Button('Clear results', id = 'clear_button',  n_clicks=0)

        ])

    return layout


