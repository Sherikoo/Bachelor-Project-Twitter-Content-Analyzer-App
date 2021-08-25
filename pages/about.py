import dash_html_components as html
import dash_bootstrap_components as dbc

layout = dbc.Jumbotron(
    [
        html.H1("What does this App do?", className="display-3", id="about-heading"),
        html.P(
            "The Twitter Content Analyzer App allows the user to analyze any tweet and decide about its veracity. "
            "The application depends on machine learning, data mining, and database. Adding explainability, "
            "descriptiveness, and interactivity was of most interest as they lack in other applications. "
            "It allows the user to compare and decide about the tweet's veracity. "
            "It allows the user to be a fact-checker.",
            className="lead", id="about-desc"
        )
    ], style={'background-color': '#8fccc9'}
)