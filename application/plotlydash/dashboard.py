import dash
from dash.dependencies import Input,Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd 
import numpy as np
from .layout import html_layout
import plotly.graph_objects as go
from application import db

def create_dashboard(server):
    """Create a Dash app"""
    dash_app = dash.Dash(server=server,
                        routes_pathname_prefix='/dashapp/',
                        external_stylesheets=['/static/dist/css/styles.css']
                        )
    # Prepare a dataset
    df = pd.read_sql_table('stores',schema='sales',con=db.engine)
    
    # Custom HTML layout
    dash_app.index_sting = html_layout


    # Create layout 
    dash_app.layout = html.Div(
        children = [
         create_data_table(df)
        ],
        id='dash-container'
    )
    return dash_app.server

def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame"""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{'name':i,'id':i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action='native',
        page_size=300
    )
    return table