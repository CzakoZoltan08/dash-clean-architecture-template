
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

from app import app, cache
from constants import TIMEOUT


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    gdpr_data = dataframe()
    filtered_df = gdpr_data[gdpr_data.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    gdpr_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    return gdpr_data.to_json(date_format='iso', orient='split')

def dataframe():
    return pd.read_json(query_data(), orient='split')