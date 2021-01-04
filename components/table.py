import dash_html_components as html

from utils.functions import formatter_2_decimals


def make_dash_table(df):
    table = []
    header = []

    for column in df.columns:
        header.append(html.Th(column))

    table.append(html.Tr(header))

    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td(formatter_2_decimals(row[i])))
        table.append(html.Tr(html_row))
    
    return table