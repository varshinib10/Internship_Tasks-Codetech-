from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("datasets/sales.csv")

# Create charts
bar_chart = px.bar(df, x="Category", y="Sales", title="Sales by Category")
pie_chart = px.pie(df, names="Category", values="Sales", title="Sales Distribution")
line_chart = px.line(df, x="Category", y="Sales", title="Sales Trend")



# App
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),

    dcc.Graph(figure=bar_chart),
    dcc.Graph(figure=pie_chart),
    dcc.Graph(figure=line_chart)
])

# Run app
app.run(debug=True)