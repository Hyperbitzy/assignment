{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP0b9ag4A+KTSZ3UexT3tJ6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Hyperbitzy/assignment/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DOv4hllCSeGP"
      },
      "outputs": [],
      "source": [
        "# Install Dash if not already installed\n",
        "!pip install dash\n",
        "\n",
        "# Import Dash and Plotly libraries\n",
        "import dash\n",
        "from dash import dcc, html\n",
        "import plotly.express as px\n",
        "import pandas as pd\n",
        "\n",
        "# Initialize the Dash app\n",
        "app = dash.Dash(__name__)\n",
        "app.title = \"Technology Trends Dashboard\"\n",
        "\n",
        "# Sample Data for Programming Languages (Current and Future)\n",
        "lang_data = pd.DataFrame({\n",
        "    'Language': ['Python', 'C++', 'Java', 'JavaScript', 'C#', 'Go', 'Rust', 'Kotlin', 'Swift', 'PHP'],\n",
        "    'Current_Usage': [16.1, 10.3, 8.5, 7.2, 6.7, 4.5, 3.0, 2.5, 2.1, 1.9],\n",
        "    'Projected_2025': [15.8, 11.2, 8.0, 6.8, 7.0, 5.0, 4.5, 3.5, 2.8, 1.5]\n",
        "})\n",
        "\n",
        "# Sample Data for Databases (Current and Future)\n",
        "db_data = pd.DataFrame({\n",
        "    'Database': ['PostgreSQL', 'MySQL', 'MongoDB', 'Oracle', 'SQL Server', 'Redis', 'SQLite', 'DynamoDB', 'Firebase', 'Cassandra'],\n",
        "    'Current_Usage': [1300, 1200, 1150, 1100, 1050, 950, 900, 850, 800, 750],\n",
        "    'Projected_2025': [1350, 1250, 1250, 1080, 1020, 1000, 950, 900, 850, 800]\n",
        "})\n",
        "\n",
        "# Sample Data for Demographics\n",
        "demographics_data = pd.DataFrame({\n",
        "    'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa'],\n",
        "    'Developers': [50000, 45000, 60000, 20000, 15000]\n",
        "})\n",
        "\n",
        "# Layout for the Dash app\n",
        "app.layout = html.Div([\n",
        "    html.H1(\"Technology Trends Dashboard\", style={'textAlign': 'center'}),\n",
        "    dcc.Tabs([\n",
        "        dcc.Tab(label='Current Technology Usage', children=[\n",
        "            html.H2('Top Programming Languages - Current Usage'),\n",
        "            dcc.Graph(figure=px.bar(lang_data, x='Language', y='Current_Usage', title='Top 10 Programming Languages (Current Year)')),\n",
        "\n",
        "            html.H2('Top Databases - Current Usage'),\n",
        "            dcc.Graph(figure=px.bar(db_data, x='Database', y='Current_Usage', title='Top 10 Databases (Current Year)'))\n",
        "        ]),\n",
        "\n",
        "        dcc.Tab(label='Future Technology Trends', children=[\n",
        "            html.H2('Projected Programming Languages (2025)'),\n",
        "            dcc.Graph(figure=px.bar(lang_data, x='Language', y='Projected_2025', title='Projected Top 10 Programming Languages (2025)')),\n",
        "\n",
        "            html.H2('Projected Databases (2025)'),\n",
        "            dcc.Graph(figure=px.bar(db_data, x='Database', y='Projected_2025', title='Projected Top 10 Databases (2025)'))\n",
        "        ]),\n",
        "\n",
        "        dcc.Tab(label='Demographics', children=[\n",
        "            html.H2('Developer Distribution by Region'),\n",
        "            dcc.Graph(figure=px.pie(demographics_data, names='Region', values='Developers', title='Global Developer Distribution'))\n",
        "        ])\n",
        "    ])\n",
        "])\n",
        "\n",
        "# Run the Dash app\n",
        "if __name__ == '__main__':\n",
        "    app.run_server(debug=True)\n"
      ]
    }
  ]
}