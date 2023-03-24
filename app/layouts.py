from dash import dcc, html
import France_Data
import dash_bootstrap_components as dbc
from callbacks import *

layout1 = html.Div([
    html.H3('France'),
    dbc.Tabs(
            [
                dbc.Tab(label="Graphe 1", tab_id="Graphe 1"),
                dbc.Tab(label="Graphe 2", tab_id="Graphe 2"),
                dbc.Tab(label="Graphe 3", tab_id="Graphe 3"),
                dbc.Tab(label="Graphe 4", tab_id="Graphe 4"),
            ],
            id="page-1-tabs",
            active_tab="Graphe 1",
        ),
    dcc.Graph(id='page-1-tab-content'),
    html.P(id='page-1-tab-value'),
    html.Div(children=[dcc.Link('Analyse France', href='./France'), dcc.Link('Analyse EU', href='./EU'), dcc.Link('Analyse Monde', href='./Monde')],
            style={'display': 'flex', 'flex-direction': 'column'})
])

""" layout1 = html.Div([
    html.H3('France'),
    dcc.Dropdown(
        {f'France - {i}': f'{i}' for i in ['PIB en fonction de l\'intensité de confinement', 'Evolution du PIB et de l\'indice d\'intensité de confinement', 'Evolution de nombre de vols passagers et de l\'intensité de confinement', 'Intensité de confinement et PIB en fonction du nombre total des cas']},
        id='page-1-dropdown'
    ),
    dcc.Graph(id='page-1-display-figure'),
    html.Div(id='page-1-display-value'),
    html.Div(children=[dcc.Link('Analyse EU', href='/EU'), dcc.Link('Analyse Monde', href='/Monde')],
            style={'display': 'flex', 'flex-direction': 'column'})
]) """

layout2 = html.Div([
    html.H3('EU'),
    dbc.Tabs(
            [
                dbc.Tab(label="Graphe 1", tab_id="Graphe 1"),
                dbc.Tab(label="Graphe 2", tab_id="Graphe 2"),
                dbc.Tab(label="Graphe 3", tab_id="Graphe 3"),
                dbc.Tab(label="Graphe 4", tab_id="Graphe 4"),
            ],
            id="page-2-tabs",
            active_tab="Graphe 1",
        ),
    dcc.Graph(id='page-2-tab-content'),
    html.P(id='page-2-tab-value'),
    html.Div(children=[dcc.Link('Analyse France', href='./France'), dcc.Link('Analyse EU', href='./EU'), dcc.Link('Analyse Monde', href='./Monde')],
            style={'display': 'flex', 'flex-direction': 'column'})
])

layout3 = html.Div([
    html.H3('Monde'),
    dbc.Tabs(
            [
                dbc.Tab(label="Graphe 1", tab_id="Graphe 1"),
                dbc.Tab(label="Graphe 2", tab_id="Graphe 2"),
                dbc.Tab(label="Graphe 3", tab_id="Graphe 3"),
                dbc.Tab(label="Graphe 4", tab_id="Graphe 4"),
            ],
            id="page-3-tabs",
            active_tab="Graphe 1",
        ),
    dcc.Graph(id='page-3-tab-content'),
    html.P(id='page-3-tab-value'),
    html.Div(children=[dcc.Link('Analyse France', href='./France'), dcc.Link('Analyse EU', href='./EU'), dcc.Link('Analyse Monde', href='./Monde')],
            style={'display': 'flex', 'flex-direction': 'column'})
])