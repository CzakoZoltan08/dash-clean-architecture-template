import dash_core_components as dcc
import dash_html_components as html

from pages.gdpr.gdpr_callbacks import dataframe, update_figure


layout = html.Div([
    html.H1("GDPR viewer"),
    html.Hr(),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=dataframe()['year'].min(),
        max=dataframe()['year'].max(),
        value=dataframe()['year'].min(),
        marks={str(year): str(year) for year in dataframe()['year'].unique()},
        step=None
    )
])