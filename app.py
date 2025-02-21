# Install Dash if not already installed
# !pip install dash

# Import Dash and Plotly libraries
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Technology Trends Dashboard"

# Sample Data for Programming Languages (Current and Future)
lang_data = pd.DataFrame({
    'Language': ['Python', 'C++', 'Java', 'JavaScript', 'C#', 'Go', 'Rust', 'Kotlin', 'Swift', 'PHP'],
    'Current_Usage': [16.1, 10.3, 8.5, 7.2, 6.7, 4.5, 3.0, 2.5, 2.1, 1.9],
    'Projected_2025': [15.8, 11.2, 8.0, 6.8, 7.0, 5.0, 4.5, 3.5, 2.8, 1.5]
})

# Sample Data for Databases (Current and Future)
db_data = pd.DataFrame({
    'Database': ['PostgreSQL', 'MySQL', 'MongoDB', 'Oracle', 'SQL Server', 'Redis', 'SQLite', 'DynamoDB', 'Firebase', 'Cassandra'],
    'Current_Usage': [1300, 1200, 1150, 1100, 1050, 950, 900, 850, 800, 750],
    'Projected_2025': [1350, 1250, 1250, 1080, 1020, 1000, 950, 900, 850, 800]
})

# Sample Data for Demographics
demographics_data = pd.DataFrame({
    'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa'],
    'Developers': [50000, 45000, 60000, 20000, 15000]
})

# Layout for the Dash app
app.layout = html.Div([
    html.H1("Technology Trends Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Current Technology Usage', children=[
            html.H2('Top Programming Languages - Current Usage'),
            dcc.Graph(figure=px.bar(lang_data, x='Language', y='Current_Usage', title='Top 10 Programming Languages (Current Year)')),

            html.H2('Top Databases - Current Usage'),
            dcc.Graph(figure=px.bar(db_data, x='Database', y='Current_Usage', title='Top 10 Databases (Current Year)'))
        ]),

        dcc.Tab(label='Future Technology Trends', children=[
            html.H2('Projected Programming Languages (2025)'),
            dcc.Graph(figure=px.bar(lang_data, x='Language', y='Projected_2025', title='Projected Top 10 Programming Languages (2025)')),

            html.H2('Projected Databases (2025)'),
            dcc.Graph(figure=px.bar(db_data, x='Database', y='Projected_2025', title='Projected Top 10 Databases (2025)'))
        ]),

        dcc.Tab(label='Demographics', children=[
            html.H2('Developer Distribution by Region'),
            dcc.Graph(figure=px.pie(demographics_data, names='Region', values='Developers', title='Global Developer Distribution'))
        ])
    ])
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)
