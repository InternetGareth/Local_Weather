import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go



# Get location data
well_locations = pd.read_csv('Data/Locations/Well_Location_Data.csv', index_col=0)
discharge_locations = pd.read_csv('Data/Locations/Discharge_Location_Data.csv', index_col=0) 
guage_locations = pd.read_csv('Data/Locations/Rain_Guage_Location_Data.csv', index_col=0) 

cols = ['Lat', 'Lon', 'Location_Key', 'Location_Type']
locations = [discharge_locations[cols], well_locations[cols],guage_locations[cols]]

all_locations = pd.concat(locations)




# get time series data
discharge_daily = pd.read_csv('Data/TimeSeries/Daily_Discharge.csv', index_col=0)
well_depths = pd.read_csv('Data/TimeSeries/Well_Depths.csv', index_col=0)
rainfall = pd.read_csv('Data/TimeSeries/Daily_Rainfall.csv', index_col=0)

time_series = [discharge_daily,well_depths,rainfall]


mapbox_token = 'pk.eyJ1IjoiaW50ZXJuZXRnYXJldGgiLCJhIjoiY2pyaWFwOTd1MDB3ZzQ0bzE2Y3B6eWkxMCJ9.9fxAtjyCT5glHuPiK8ee0Q'

px.set_mapbox_access_token(mapbox_token)
well_map = px.scatter_mapbox (all_locations, 
lat="Lat", 
lon="Lon", 
hover_name = 'Location_Key',
color='Location_Type',
color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)




app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Wells of Kitsap'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(id='wellmaps', figure=well_map),
    dcc.Graph(id='well chart'),
    html.Div(id='my-div')])


@app.callback(Output('well chart','figure'), [Input('wellmaps', 'clickData')])
def plot_well_data(clickdata):

    if clickdata is None:
        i =  0
        j = 0
    else:
        i = clickdata['points'][0]['pointNumber']
        j = clickdata['points'][0]['curveNumber'] 

    selected_site = locations[j].iloc[i,:]['Location_Key']
    selected_data = time_series[j]

    site_mask = selected_data['Location_Key'] == selected_site
    selected_site_data = selected_data[site_mask]

    if j == 0:
        data = selected_site_data['Avg Discharge (cfs)']
        name = selected_site_data['Station'][0]
    
    elif j == 1:
        data = selected_site_data['Water Level +/- MSL']
        name = selected_site_data['Well Name'][0][8:]

    elif j == 2:
        data = selected_site_data['Rain(inches)']
        name = selected_site_data['Station Name'][0]

    data = data.sort_index()

    well_depth = go.Scatter(
        x=data.index,
        y=data.values,
        name = name,
        line = dict(color = '#7F7F7F'),
        opacity = 0.8)



    well_layout = dict(
        title= name,
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

    well_fig = dict(data=[well_depth], layout=well_layout)
    return well_fig


if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)