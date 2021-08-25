import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


from app import app
from pages import home, about, contact, usage

# The navigation bar
navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src='/assets/logo.png', id='logo'))
                ],
                align="center",
            ),
            href="/home",
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/home", className="nav-item"),
                dbc.NavLink("How to Use", href="/usage", className="nav-item"),
                dbc.NavLink("About", href="/about", className="nav-item"),
                dbc.NavLink("Contact", href="/contact", className="nav-item")
            ],
            className="ml-auto"
        )
    ], color="#f2f2f2", id="navbar"
    , sticky="top"
)

# The layout that holds the whole page's content.
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/contact':
        return contact.layout
    elif pathname == '/about':
        return about.layout
    elif pathname == '/usage':
        return usage.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)