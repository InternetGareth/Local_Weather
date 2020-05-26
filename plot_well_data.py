import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

trace_low = go.Scatter(
    x=selected_well.index,
    y=selected_well.values,
    name = "welldepth",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)




layout = dict(
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

fig = dict(data=trace_low, layout=layout)

# Now here's the Dash part:

dash.layout = html.Div([
    dcc.Graph(id='my-graph', figure=fig)
])