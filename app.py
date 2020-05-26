import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Get well data
filename = "KPUD_Well_Depth_2020_04_05.csv"
well_depths=pd.read_csv(filename, index_col=0)
well_depths.index = pd.to_datetime(well_depths.Date)
well_depths  = well_depths.drop('Date', axis=1)
wells_in_df = well_depths['Well Name'].unique()
well_mask = well_depths['Well Name'] == wells_in_df[3]
selected_well = well_depths['Water Level +/- MSL'][well_mask]

# set up Dash page

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


well_data = go.Scatter(
    x=selected_well.index,
    y=selected_well.values,
    name = "welldepth",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)




well_layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)

fig = dict(data=[well_data], layout=well_layout)


app.layout = html.Div(children=[
    html.H1(children='Wells of Kitsap'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(id='my-graph', figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)