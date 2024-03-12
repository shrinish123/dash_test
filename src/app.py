from dash import Dash, html, dcc

app = Dash(__name__,suppress_callback_exceptions=True)
app.title = 'Sicomoro'
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

if __name__ == '__main__':
    app.run_server()
