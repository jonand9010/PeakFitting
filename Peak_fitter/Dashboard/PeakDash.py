import dash


from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

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


@Peak_fit_dashboard.callback(Output('Model-fit-plot', 'figure'), Output('Residuals-plot', 'figure'), Input('data-import', 'contents'))  
def plot_model_fit(data):

    datafile = read_datafile(data)

    try: 
        df = pd.read_csv(datafile, sep = ';', names = ['x', 'y'])
    
        model = poly2()
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