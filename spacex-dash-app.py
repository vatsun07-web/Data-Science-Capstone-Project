
# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv('spacex_launch_dash.csv')
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

launch_sites = spacex_df['Launch Site'].unique().tolist()
# Added 'ALL' to the list of options
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
                   [{'label': site, 'value': site} for site in launch_sites]

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection
    # The default select value is for ALL sites
    # dcc.Dropdown(id='site-dropdown',...)
    html.Div([
        html.Label("Select Launch Site:"),
        dcc.Dropdown(
            id='site-dropdown',  # FIXED: Changed from 'site_dropdown' to 'site-dropdown' to match callback
            options=dropdown_options,
            value='ALL',
            placeholder="Select a Launch Site",
            searchable=True
        )
    ]),
    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    # If a specific launch site was selected, show the Success vs. Failed counts for the site
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: Add a slider to select payload range
    #dcc.RangeSlider(id='payload-slider',...)
    dcc.RangeSlider(
        id='payload-slider',
        min=0, 
        max=10000, 
        step=1000,
        # FIXED: Generates marks for every 1000kg (0, 1000, 2000...)
        marks={i: f'{i}' for i in range(0, 10001, 1000)},
        value=[min_payload, max_payload]
    ),
    
    html.Br(),

    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Pie chart for All Sites: Shows total success count contributed by each site
        fig = px.pie(
            spacex_df, 
            values='class', 
            names='Launch Site', 
            title='Total Successful Launches By Site'
        )
        return fig
    else:
        # Pie chart for Specific Site: Shows Success (1) vs Failure (0)
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        
        # Calculate the counts for success vs failure
        site_counts = filtered_df['class'].value_counts().reset_index() 
        site_counts.columns = ['class', 'count']
        
        fig = px.pie(
            site_counts, 
            values='count',
            names='class',
            title=f'Total Successful vs. Failed Launches for site {entered_site}',
            # Using discrete map ensures 1 is always Green and 0 is always Red
            color='class',
            color_discrete_map={0: 'red', 1: 'green'}
        )
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), 
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    
    # 1. Filter by Payload Range (Always applies)
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    # 2. Filter by Site (Conditionally applies)
    if entered_site == 'ALL':
        # No extra filtering needed
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Correlation between Payload and Success for All Sites',
            labels={'class': 'Launch Outcome (0=Failure, 1=Success)'}
        )
    else:
        # Filter for the specific site
        site_filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        
        fig = px.scatter(
            site_filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Correlation Between Payload and Success for {entered_site}',
            labels={'class': 'Launch Outcome (0=Failure, 1=Success)'}
        )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run()