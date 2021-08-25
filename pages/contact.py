import dash_html_components as html
import dash_bootstrap_components as dbc

layout = dbc.Jumbotron(
    [
        html.H1("Contact Us", className="display-4"),
        html.P(
            "We'd love to hear from you.",
            className="lead",
        )
    ], style={'background-image': 'url("/assets/contact.jfif")', 'background-size': 'cover',
              'height': '400px', 'font-weight': 'bold'}
)