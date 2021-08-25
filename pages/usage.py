import dash_html_components as html
import dash_bootstrap_components as dbc

# A page illustrates how the App is being used.

layout = html.Div(
    [
        dbc.Jumbotron(
            [
                html.H1("How to use the App?", className="display-3", id="usage-heading"),
                html.P(
                    "The app is easy to use. Please follow these steps.",
                    className="lead", id="usage-desc"
                )
            ], className="mt-5"
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 1", className="card-title"),
                    html.P(
                        "Open twitter.com and select any tweet written in English.",
                        className="card-text",
                    )
                ]
            ), className="m-5 w-75 odd card-body", outline=True, color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 2", className="card-title"),
                    html.P(
                        "Copy the tweet's ID or the whole URL - both work.",
                        className="card-text",
                    ),
                    html.Img(src="/assets/use-1.png", width='80%', height='30%')
                ]
            ), className="m-5 w-75 even card-body", color='rgb(242, 242, 242)'
            ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 3", className="card-title"),
                    html.P(
                        "Paste the ID or the URL the shown box and then press the button 'GO'.",
                        className="card-text",
                    ),
                    html.Img(src="/assets/use-2.png", width='100%', height='100%')
                ]
            ), className="m-5 w-75 odd card-body", color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 4", className="card-title"),
                    html.P(
                        "The page will load for several seconds, then you will see the results. Please be patient.",
                        className="card-text",
                    )
                ]
            ), className="m-5 w-75 even card-body", color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 5", className="card-title"),
                    html.P(
                        "You can hover over the info buttons to have a better understanding of the shown results.",
                        className="card-text",
                    ),
                    html.Img(src="/assets/use-3.png", width='70%', height='40%')
                ]
            ), className="m-5 w-75 odd card-body", color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 6", className="card-title"),
                    html.P(
                        "Select one of the 3 categories shown and press the button 'Get Similar Tweets' to get similar "
                        "tweets from our database.",
                        className="card-text",
                    ),
                    html.Img(src="/assets/use-4.png", width='100%', height='100%')
                ]
            ), className="m-5 w-75 even card-body", color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 7", className="card-title"),
                    html.P(
                        "A graph of points will be shown. Each point represents a tweet. The distance between each "
                        "tweet and the centered tweet expresses the similarity between them. The black centered point represents your "
                        "analyzed tweet, the green points represent real tweets, while the red points "
                        "represent fake tweets.",
                        className="card-text",
                    ),
                    html.Img(src="/assets/use-5.png", width='50%', height='50%')
                ]
            ), className="m-5 w-75 odd card-body", color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Step 8", className="card-title"),
                    html.P(
                        "Click on each point on the graph to see it's text and compare its characteristics to your analyzed tweet.",
                        className="card-text",
                    )
                ]
            ), className="m-5 w-75 even card-body", color='rgb(242, 242, 242)'
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Final Step", className="card-title"),
                    html.P(
                        "We will not assess the tweet. You have the data and it is your own decision.",
                        className="card-text",
                    )
                ]
            ), className="m-5 w-75 odd card-body", color='rgb(242, 242, 242)'
        ),
    ]

    , id="usage-main-div"
)