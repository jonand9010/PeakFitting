
import dash_html_components as html
import dash_core_components as dcc

def App_Layout():
    layout = html.Div([
        html.Div([
        html.H1('Peak fitting'),
        dcc.Upload(id = 'data-import', children = html.Div(['Drag and Drop or ', html.A('Select File')]),
                    style = {'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px',
            'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}, multiple = False)
        ]),
        

        dcc.Graph(id = 'Raw-data-plot'),


        dcc.Graph(id = 'Model-fit-plot'),

        dcc.Graph(id = 'Residuals-plot')

        ])

    return layout

