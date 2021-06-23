import dash


from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

import numpy as np
import pandas as pd
from inspect import getmembers, isclass

from layouts.app_layout import App_Layout
from gui_utils.helper_functions import read_datafile, model_selection, Table
import dash_table
from dash_table.Format import Format


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
Peak_fit_dashboard = dash.Dash(__name__, external_stylesheets = external_stylesheets)

Peak_fit_dashboard.layout = App_Layout()
Table_fitresults = Table()

@Peak_fit_dashboard.callback(Output('Raw-data-plot', 'figure'), Input('data-import', 'contents'))
def plot_raw_data(data):

    datafile = read_datafile(data)

    try:
        df = pd.read_csv(datafile, sep = ';', names = ['x', 'y'])

        fig = px.scatter(df, x = df['x'], y = df['y'])

    except:
        fig = go.Figure()

    return fig


@Peak_fit_dashboard.callback(Output('Model-fit-plot', 'figure'), Output('Residuals-plot', 'figure'), Output('Fit-Results', 'data'),
                            Output('Fit-Results', 'columns'), [Input('data-import', 'contents'), Input('Model-selection', 'value'), 
                            Input('Raw-data-plot', 'relayoutData')] ) 
def plot_model_fit(data, model_str, relayout_data, *figures):

    datafile = read_datafile(data)

    try: 
        df = pd.read_csv(datafile, sep = ';', names = ['x', 'y'])
        
        model = model_selection(model_str)
        
        model.fit(df['x'], df['y'])    

        Table_fitresults.update_table(model.parameters)

        fig_model = px.scatter(df, x = 'x', y = 'y')
        
        fig_model.add_scatter(x = df['x'], y = model.predict(df['x']), mode='lines')
        fig_model.update_layout(showlegend=False)

        df['residuals'] = df['y'] - model.predict(df['x'])
        fig_residuals = px.scatter(df, x = 'x', y = df['residuals'])

    except:

        fig_model = go.Figure()
        fig_residuals = go.Figure()

    for fig in [fig_model, fig_residuals]:
        try:
            fig['layout']["xaxis"]["range"] = [relayout_data['xaxis.range[0]'], relayout_data['xaxis.range[1]']]
            fig['layout']["xaxis"]["autorange"] = False
        except (KeyError, TypeError):
            fig['layout']["xaxis"]["autorange"] = True


    return fig_model, fig_residuals, Table_fitresults.data, Table_fitresults.columns


@Peak_fit_dashboard.callback(Output('clear_button', 'n_clicks'), Input('clear_button', 'n_clicks'))
def update_output(n_clicks):
    if n_clicks > 0:
        Table_fitresults = Table()
        n_clicks = 0
    return n_clicks
    

if __name__ == '__main__': Peak_fit_dashboard.run_server(debug=True)