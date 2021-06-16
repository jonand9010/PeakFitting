import dash


from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px


import pandas as pd
from inspect import getmembers, isclass

from layouts.app_layout import App_Layout
from gui_utils.parse_datafile import read_datafile
from models.fit_profiles import poly2



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
Peak_fit_dashboard = dash.Dash(__name__, external_stylesheets = external_stylesheets)

Peak_fit_dashboard.layout = App_Layout()

@Peak_fit_dashboard.callback(Output('Raw-data-plot', 'figure'), Input('data-import', 'contents'))
def plot_raw_data(data):

    datafile = read_datafile(data)

    try:
        df = pd.read_csv(datafile, sep = ';', names = ['x', 'y'])

        fig = px.scatter(df, x = df['x'], y = df['y'])

    except:
        fig = go.Figure()

    return fig


def model_selection(model_str):
    from models import fit_profiles
    profiles = getmembers(fit_profiles, isclass)
    
    for i in range(len(profiles)):
        
        if profiles[i][0] == model_str:
            model = profiles[i][1]()

    return model


@Peak_fit_dashboard.callback(Output('Model-fit-plot', 'figure'), Output('Residuals-plot', 'figure'), 
                            Input('data-import', 'contents'), Input('Model-selection', 'value'))  
def plot_model_fit(data, model_str):

    datafile = read_datafile(data)

    try: 
        df = pd.read_csv(datafile, sep = ';', names = ['x', 'y'])
        
        model = model_selection(model_str)

        model.fit(df['x'], df['y'])
        
        fig_model = px.scatter(df, x = 'x', y = 'y')
        
        fig_model.add_scatter(x = df['x'], y = model.predict(df['x']), mode='lines')

        df['residuals'] = df['y'] - model.predict(df['x'])
        fig_residuals = px.scatter(df, x = 'x', y = df['residuals'])

    except:

        fig_model = go.Figure()
        fig_residuals = go.Figure()

    return fig_model, fig_residuals


if __name__ == '__main__': Peak_fit_dashboard.run_server(debug=True)