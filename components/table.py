import dash_html_components as html

from utils.functions import formatter_2_decimals


def make_dash_table(df):
    body = []
    header = []

    for column in df.columns:
        header.append(html.Th(column))

    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td(formatter_2_decimals(row[i])))
        body.append(html.Tr(html_row))
    
    tHead = html.Thead(html.Tr(header))
    tBody = html.Tbody(body)
    table = html.Table([tHead, tBody])

    return table