import pandas as pd

from app import cache
from utils.constants import TIMEOUT


@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    gdp_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    return gdp_data.to_json(date_format='iso', orient='split')

def dataframe():
    return pd.read_json(query_data(), orient='split')