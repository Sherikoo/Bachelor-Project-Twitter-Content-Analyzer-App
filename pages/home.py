import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from classes import Tokens, Model
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import plotly.graph_objs as go

from app import app


# A function reads the "User_Characteristics" and returns it in a suitable form.
def user_characteristics_datasets():
    user_characteristics = pd.read_excel('User_Characteristics.xlsx')
    user_characteristics_true_false = user_characteristics.drop(['id', 'text'], axis=1, inplace=False)
    user_characteristics_with_claim = user_characteristics_true_false.copy(deep=True)
    user_characteristics_without_claim = user_characteristics_true_false.copy(deep=True)

    user_characteristics_without_claim.drop(['veracity'], axis=1, inplace=True)

    verified_arr_1 = []
    for f in user_characteristics_with_claim['verified']:
        if f:
            verified_arr_1.append(1)
        else:
            verified_arr_1.append(0)
    user_characteristics_with_claim['verified'] = verified_arr_1

    claim_arr = []
    for f in user_characteristics_with_claim['veracity']:
        if f:
            claim_arr.append(1)
        else:
            claim_arr.append(0)
    user_characteristics_with_claim['veracity'] = claim_arr

    verified_arr_2 = []
    for f in user_characteristics_without_claim['verified']:
        if f:
            verified_arr_2.append(1)
        else:
            verified_arr_2.append(0)
    user_characteristics_without_claim['verified'] = verified_arr_2

    dataset_dict = {
        'user_char': user_characteristics,
        'user_char_true_false': user_characteristics_true_false,
        'user_char_with_claim': user_characteristics_with_claim,
        'user_char_without_claim': user_characteristics_without_claim
    }

    return dataset_dict

# A function gets the "User Characteristics" of the analyzed tweet amd returns it in a suitable form.
def get_user_char():
    tweets_count = content["tweetsCount"]
    followers_count = content['user_followers_count']
    following_count = content['user_following_count']
    listed_count = content['user_listed_count']
    favourites_count = content['user_favourites_count']
    verified = content['verified']
    account_age_in_days = content['age']
    avg_tweets_count = content['avg']


    if verified:
        verified = 1
    else:
        verified = 0

    new_tweet = pd.DataFrame(data={
        'account_age_in_days': [account_age_in_days],
        'followers_count': [followers_count],
        'following_count': [following_count],
        'listed_count': [listed_count],
        'favourites_count': [favourites_count],
        'verified': [verified],
        'tweets_count': [tweets_count],
        'avg_tweets_count': [avg_tweets_count]
    })

    new_tweet_true_false = new_tweet.copy(deep=True)
    verified_array = []
    for v in new_tweet_true_false['verified']:
        if v == 1:
            verified_array.append('True')
        else:
            verified_array.append('False')
    new_tweet_true_false['verified'] = verified_array
    new_tweet_true_false['veracity'] = '-'
    new_tweet_dict = {
        'new_tweet_true_false': new_tweet_true_false,
        'new_tweet': new_tweet
    }

    return new_tweet_dict

# A function reads the "Tweet Characteristics" and returns it in a suitable form.
def tweet_characteristics_datasets():
    tweet_characteristics = pd.read_excel('Tweet_Characteristics.xlsx')
    tweet_characteristics_true_false = tweet_characteristics.drop(['id', 'text'], axis=1, inplace=False)
    tweet_characteristics_with_claim = tweet_characteristics_true_false.copy(deep=True)
    tweet_characteristics_without_claim = tweet_characteristics_true_false.copy(deep=True)

    tweet_characteristics_without_claim.drop(['veracity'], axis=1, inplace=True)

    claim_arr = []
    for f in tweet_characteristics_with_claim['veracity']:
        if f:
            claim_arr.append(1)
        else:
            claim_arr.append(0)
    tweet_characteristics_with_claim['veracity'] = claim_arr


    dataset_dict = {
        'tweet_char': tweet_characteristics,
        'tweet_char_true_false': tweet_characteristics_true_false,
        'tweet_char_with_claim': tweet_characteristics_with_claim,
        'tweet_char_without_claim': tweet_characteristics_without_claim
    }

    return dataset_dict

# A function gets the "Tweet Characteristics" of the analyzed tweet amd returns it in a suitable form.
def get_tweet_content():
    retweet_count = content['retweet_count']
    favorite_count = content['favorite_count_knn']
    uppercase_words_count = content['upcount']
    hashtags_count = content['nhashtags']
    urls_count = content['nurls']
    mentions_count = content['mentions_count']
    emojis_count = content['nemojis']


    new_tweet = pd.DataFrame(data={
        'retweet_count': [retweet_count],
        'favorite_count': [favorite_count],
        'uppercase_words_count': [uppercase_words_count],
        'hashtags_count': [hashtags_count],
        'urls_count': [urls_count],
        'mentions_count': [mentions_count],
        'emojis_count': [emojis_count]
    })

    new_tweet_true_false = new_tweet.copy(deep=True)
    new_tweet_true_false['veracity'] = '-'

    new_tweet_dict = {
        'new_tweet_true_false': new_tweet_true_false,
        'new_tweet': new_tweet
    }

    return new_tweet_dict

# A function reads the "NLP Features" and returns it in a suitable form.
def form_features_dataset():
    features = pd.read_excel('NLP_Features.xlsx')
    features_with_claim = features.drop(['id', 'text'], axis=1, inplace=False)
    features_without_claim = features.drop(['id', 'text', 'veracity'], axis=1, inplace=False)

    features_true_false = features_with_claim.copy(deep=True)
    claim_array = []
    for target in features_true_false['veracity']:
        if target == 1:
            claim_array.append('True')
        else:
            claim_array.append('False')
    features_true_false['veracity'] = claim_array

    dataset_dict = {
        'features': features,
        'features_true_false': features_true_false,
        'features_with_claim': features_with_claim,
        'features_without_claim': features_without_claim
    }

    return dataset_dict


# A function gets the "NLP Features" of the analyzed tweet amd returns it in a suitable form.
def get_tweet_features():
    sentiment = content['Sentiment']
    hate_speech = content['Hate Speech']
    subjectivity = content['Subjectivity']

    new_tweet = pd.DataFrame(data={
        'Sentiment (%)': [sentiment],
        'Hate Speech (%)': [hate_speech],
        'Subjectivity (%)': [subjectivity]
    })

    new_tweet_true_false = new_tweet.copy(deep=True)
    new_tweet_true_false['veracity'] = '-'

    new_tweet_dict = {
        'new_tweet_true_false': new_tweet_true_false,
        'new_tweet': new_tweet
    }

    return new_tweet_dict

# A function performs the K-NN and returns similar tweets and their distances.
def scale_and_knn(dataset_with_claim, dataset_without_claim, tweet):
    scaler = StandardScaler()
    scaled_user_dataset= scaler.fit_transform(dataset_without_claim)
    knn = NearestNeighbors(n_neighbors=10)
    knn.fit(scaled_user_dataset)
    scaled_user_tweet = scaler.transform(tweet)
    distances, nearest_neighbors = knn.kneighbors(scaled_user_tweet)
    neighbors_dataframe = dataset_with_claim.loc[nearest_neighbors[0]]
    false_indices = neighbors_dataframe.index[neighbors_dataframe['veracity'] == 0].tolist()
    true_indices = neighbors_dataframe.index[neighbors_dataframe['veracity'] == 1].tolist()

    r_and_theta = {
        'distances': distances,
        'true_indices': true_indices,
        'false_indices': false_indices
    }
    return r_and_theta

# A function draws the K-NN graph of the analyzed tweet against 10 similar tweets.
def draw_graph(r_and_theta):
    return dcc.Graph(
                id='tweets-graph',
                figure={
                    'data': [
                        go.Scatterpolar(
                            r = r_and_theta['distances'][0],
                            theta = r_and_theta['false_indices'],
                            mode = 'markers',
                            marker = {
                                'size': 24,
                                'color': 'red',
                                'line': {'width': 1, 'color': 'black'}
                                },
                            opacity=0.6,
                            name = 'A Fake Tweet',
                            text = 'A Fake Tweet',
                            hoverinfo = 'text',
                        ),
                        go.Scatterpolar(
                            r =  r_and_theta['distances'][0],
                            theta = r_and_theta['true_indices'],
                            mode = 'markers',
                            marker = {
                                'size': 24,
                                'color': 'green',
                                'line': {'width': 1, 'color': 'black'}
                                },
                            opacity=0.6,
                            name = 'A Real Tweet',
                            text = 'A Real Tweet',
                            hoverinfo = 'text',
                        ),
                        go.Scatterpolar(
                            r = [0],
                            theta = [0.5],
                            mode = 'markers',
                            marker = {
                                'size': 24,
                                'color': 'black',
                                'line': {'width': 1, 'color': 'grey'}
                                },
                            name = 'The Analyzed Tweet',
                            text = 'The Analyzed Tweet',
                            hoverinfo = 'text',
                        )
                    ],

                    'layout': go.Layout(
                        showlegend= False,
                        hovermode='closest',
                        # paper_bgcolor = '#252433',
                        paper_bgcolor= '#9ebfd9',
                        # paper_bgcolor='#8dacb3',
                        # paper_bgcolor='#77d7ed',
                        title = 'Click to show text and compare characteristics:',
                        font_family = 'Rockwell',
                        font_size = 13,
                        # font_color = '#e6e0d8',
                        font_color='white',
                        # font_color = '#2196f3',
                        polar = dict(
                            bgcolor = "rgb(223, 223, 223)",
                            angularaxis = dict(
                                linewidth = 1,
                                showline=True,
                                linecolor='white',
                                showticklabels=False,
                                visible = False
                                ),
                            radialaxis = dict(
                                side = "counterclockwise",
                                showline = False,
                                linewidth = 2,
                                gridcolor = "white",
                                gridwidth = 2,
                                showticklabels=False,
                                ticks=''
                                )
                        )
                    )
                }
            )

# A function draws the comparison table between the analyzed tweet and the clicked tweet.
def draw_table(tweet_index, dataset, tweet, table_type):
        return dbc.Table([
                html.Thead(html.Tr([html.Th(table_type), html.Th("Analyzed Tweet"), html.Th("Clicked Tweet")]))
                ]
                +
                [
                    html.Tbody([
                        html.Tr(
                            [
                                html.Td(
                                    col, className="feature-column"
                                ),
                                html.Td(
                                    tweet[col], className="data-column"
                                ),
                                html.Td(
                                    str(dataset.iloc[tweet_index][col]), className="data-column"
                                )
                            ]
                        )
                        for col in dataset.columns
                    ])
                ], striped=True, hover=False, size="md", className="comparison-tables"
            )

def draw_table_same(tweet, table_type):
    return dbc.Table([
                         html.Thead(html.Tr([html.Th(table_type), html.Th("Analyzed Tweet"), html.Th("Clicked Tweet")]))
                ]
                +
                [
                    html.Tbody([
                        html.Tr(
                            [
                                html.Td(
                                    col, className="feature-column"
                                ),
                                html.Td(
                                    tweet[col]
                                ),
                                html.Td(
                                    tweet[col]
                                )
                            ]
                        )
                        for col in tweet.columns
                    ])
                ], striped=True, hover=False, size="md", className="comparison-tables"
        )

# The layout of the whole page's content.
# It is empty and built using the callback functions.
layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Label("Analyze your Tweet here:",
                      className="ml-5 mt-3 pl-3", id="form-label")
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Input(type="text",
                                  placeholder="Enter Tweet ID or URL ... (e.g. 1376196131777089546  or  https://twitter.com/POTUS/status/1376196131777089546)",
                                  bs_size="lg", id="input-id")),
                dbc.Col(
                    dbc.Button("Go", color="primary", className="ml-2", size="lg", id="submit-button", disabled=True),
                    width="auto",
                ),
            ],
            no_gutters=True,
            className="py-3 px-5",
            align="center",
            id="form-row"
        )
    ], fluid=True, className="mt-4 my-5", id="form-container"),

    dcc.Loading(
        dbc.Container([
            html.Div([
                dbc.Modal(
                [
                    dbc.ModalHeader("Attention!", style={'font-size': '24px'}),
                    dbc.ModalBody("The requested Tweet does not exist!  Please enter a valid Tweet ID or URL!"),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="error-close", className="ml-auto")
                    ),
                ],
                id="error-modal", size='lg'
                )
            ]),
            dbc.Row([
                dbc.Col(html.Div(id="tweet-frame-heading", className="table-heading"), width='4'),
                dbc.Col(html.Div(id="user-table-heading", className="table-heading"), width='4'),
                dbc.Col(html.Div(id="tweet-table-heading", className="table-heading"), width='4')
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(id="inserted-tweet", className="mr-2"), width='4', id="inserted-tweet-col", className="data-tables-col"
                ),
                dbc.Col(
                    html.Div(id="user-data-table"), width='4', id="user-data-col", className="data-tables-col"
                ),
                dbc.Col(
                    html.Div(id="content-data-table", className="ml-2"), width='4', id="content-data-col", className="data-tables-col"
                )
            ], id="data-tables-row"),
            html.Div(html.Div(id="features-heading"), className="mt-5 ml-1 mb-3"),
            dbc.Row([
                dbc.Col(
                    html.Div(id="inference-features"), width='3'
                ),
            dbc.Col(
                    html.Div(id="inference-progress"), width='9'
                )
            ], className="my-5", id="features-row")
        ], fluid=True, className="my-5", id="tables-container")
        , type="dot", className="loading-main"
    ),

    dbc.Container([
        dbc.Row(html.Div(id="knn-heading")),
        html.Div(id="knn-form-row")
    ], fluid=True, className="my-5", id="knn-form-container"),
    dbc.Container([

    ], fluid=True, className="my-4", id="knn-container"),
    dbc.Container(
        html.Footer("Universität Duisburg-Essen \u00a9 2021")
    )

], id="page-container")

# The main callback function.
# After the 'GO button is being clicked, it returns the 'User Characteristics',
# 'Tweet Characteristics', and 'NLP Features' data.
@app.callback(
    [Output('inserted-tweet', 'children'),
     Output('tweet-frame-heading', 'children'),
     Output('user-data-table', 'children'),
     Output('user-table-heading', 'children'),
     Output('tweet-table-heading', 'children'),
     Output('content-data-table', 'children'),
     Output('features-heading', 'children'),
     Output('inference-progress', 'children'),
     Output('inference-features', 'children'),
     Output('knn-heading', 'children'),
     Output('knn-form-row', 'children'),
     Output('knn-container', 'children'),
     Output("error-modal", "is_open")],
    [Input('submit-button', 'n_clicks'),
     Input("error-close", "n_clicks")],
    [State('input-id', 'value'),
     State("error-modal", "is_open")]
)
def get_tweet_data(n1, n2, value, is_open1):
    if n1:
        if value.isnumeric():
            ID = value
        else:
            ID = value.split('/')[-1]
        T = Tokens.T
        T.id = ID
        M = Model.M
        id_valid = T.get_tweet_object(T)
        embedded_tweet = T.getEmbedTweet(T)
        if id_valid == 0:
            public_metrics = M.get_public_metrics(M, ID)
            global content
            content = {'x': 50, 'id': ID, 'accountName': T.name, 'followers': T.followers, 'following': T.following,
                       'nhashtags': M.parse(M, 1), 'nemojis': M.parse(M, 2), 'nurls': M.parse(M, 3),
                       'hashtags': M.parse(M, 4), 'emojis': M.parse(M, 5), 'urls': M.parse(M, 6),
                       'upcount': M.Upcount(M),
                       'Sentiment': M.predict_sentiment(M),
                       'Hate Speech': M.predict_hate_speech(M),
                       'Subjectivity': M.predict_subjectivity(M),
                       'created_at': T.created_at.date(),
                       'descr': T.descr, 'verified': T.verified, 'tweetsCount': T.tweets, 'age': T.userAge,
                       'avg': T.avgPerDay,
                       'img': T.img, 'tweetEmbed': embedded_tweet, 'favoriteCount': T.favorite_count,
                       'idprint': T.id,
                       'retweet_count': public_metrics['retweet_count'], 'reply_count': public_metrics['reply_count'],
                       'quote_count': public_metrics['quote_count'],
                       'favorite_count_knn': T.favorite_count_knn, 'user_followers_count': T.followers_knn,
                       'user_following_count': T.following_knn, 'user_listed_count': T.user_listed_count_knn,
                       'user_favourites_count': T.user_favourites_count, 'mentions_count': T.user_mentions_count,
                       'analyzed_text': T.text
                       }

            user_table_heading = dbc.Row([
                dbc.Col(html.Div("User Characteristics", className="tables-headings", id="user-info-div1"),
                        id="user-info-col1", width="8"),
                dbc.Col(html.Div(
                    [
                        dbc.Button("?", id="user-char-info-btn", outline=True, className="info-button ml-0", size="sm"),
                        dbc.Tooltip(
                            "User Characteristics are the meta-features of the user who owns the "
                            "analyzed tweet.",
                            target="user-char-info-btn",
                            placement="top-start",
                            id="tooltip-user-char",
                            style={'font-size': '16px'}
                        )
                    ], className="info-div", id="user-info-div2")
                    , className="info-col", id="user-info-col2", width="4")
            ], id="user-table-heading-div")

            tweet_table_heading = dbc.Row([
                dbc.Col(html.Div("Tweet Characteristics", className="tables-headings", id="tweet-info-div1"),
                        id="tweet-info-col1", width="8"),
                dbc.Col(html.Div(
                    [
                        dbc.Button("?", id="tweet-char-info-btn", outline=True, className="info-button ml-0", size="sm"),
                        dbc.Tooltip(
                            "Tweet Characteristics are the tweet content features and tweet metadata.",
                            target="tweet-char-info-btn",
                            placement="top-start",
                            id="tooltip-tweet-char",
                            style={'font-size': '16px'}
                        )
                    ], className="info-div", id="tweet-info-div2")
                    , className="info-col", id="tweet-info-col2", width="4")
            ], id="tweet-table-heading-div")

            tweet_frame_heading = html.Div("The Analyzed Tweet", className="tables-headings", id="analyzed-tweet-heading")

            user_data_table = html.Div(
                dbc.Table(
                    [
                        html.Tbody([
                            html.Tr([html.Td("Account Name"), html.Td(content['accountName'])]),
                            html.Tr([html.Td("Profile Picture"),
                                     html.Td(html.Div([
                                dbc.Button(html.Img(src=content['img']), id="img-button"),
                                dbc.Modal(
                                    [
                                        # dbc.ModalHeader("Header"),
                                        dbc.ModalBody(html.Iframe(src="https://twitframe.com/show?url=" + content['tweetEmbed']
                                                                  , height='100%', width='100%', className="tweet-frame")
                                                      , id="tweet-modal-body"),

                                        dbc.ModalFooter(
                                            dbc.Button(
                                                "Close", id="tweet-close", className="ml-auto"
                                            )
                                        ),
                                    ],
                                    id="tweet-modal",
                                    centered=True,
                                    size='lg'
                                )
                            ]))]),
                            html.Tr([html.Td("Number of followers"), html.Td(content['followers'])]),
                            html.Tr([html.Td("Number of following"), html.Td(content['following'])]),
                            html.Tr([html.Td("Account created on"), html.Td(content['created_at'])]),
                            html.Tr([html.Td("Verified"), html.Td(str(content['verified']))]),
                            html.Tr([html.Td("Tweets Count"), html.Td(content['tweetsCount'])]),
                            html.Tr([html.Td("Favourites Count"), html.Td(content['user_favourites_count'])]),
                            html.Tr([html.Td("Listed Count"), html.Td(content['user_listed_count'])]),
                            html.Tr([html.Td("Account Age (in days)"), html.Td(content['age'])]),
                            html.Tr([html.Td("Average Tweets per day"), html.Td(content['avg'])])
                        ])
                    ], striped=True, hover=False, size="sm"
                ), className="tables"
            )

            content_data_table = html.Div(
                dbc.Table(
                    [
                        html.Tbody([
                            html.Tr([html.Td("Number of Hashtags"), html.Td(content['nhashtags'])]),
                            html.Tr([html.Td("Hashtags"), html.Td(content['hashtags'])]),
                            html.Tr([html.Td("Number of Emojis"), html.Td(content['nemojis'])]),
                            html.Tr([html.Td("Emojis"), html.Td(content['emojis'])]),
                            html.Tr([html.Td("Number of URLs"), html.Td(content['nurls'])]),
                            html.Tr([html.Td("URLs"), html.Td(content['urls'])]),
                            html.Tr([html.Td("Number of Uppercase Words"), html.Td(content['upcount'])]),
                            html.Tr([html.Td("Number of Likes"), html.Td(content['favoriteCount'])]),
                            html.Tr([html.Td("Number of Retweets"), html.Td(content['retweet_count'])]),
                            html.Tr([html.Td("Number of Comments"), html.Td(content['reply_count'])]),
                            html.Tr([html.Td("Number of Quotes"), html.Td(content['quote_count'])])
                        ])
                    ], striped=True, hover=False, size="sm", id="tweet-char-table"
                ), className="tables"
            )

            features_heading = dbc.Row([
                dbc.Col(html.Div("After review, the analyzed tweet may contain: (NLP Features)"
                                 , id="feature-heading-div", className="mr-0")
                        , id="feature-heading-col", width="6"),
                dbc.Col(html.Div(
                    [
                        dbc.Button("?", id="feature-info-btn", outline=True, className="info-button ml-0", size="sm"),
                        dbc.Tooltip(
                            "NLP stands for Natural Language Processing. The NLP Features are the tweet's sentiment "
                            "features calculated by processing the tweet's text.",
                            target="feature-info-btn",
                            placement="top-start",
                            id="tooltip-feature",
                            style={'font-size': '16px'}
                        )
                    ], id="feature-info-div", className="info-div ml-0"
                ), id="feature-info-col", className="info-col", width="6")
            ], id="feature-heading-main-div")


            features_items = [
                dbc.Row([
                    dbc.Col(
                        html.Div('Sentiment', className="feature ml-0", style={'background-color': '#dc3545'})),
                    dbc.Col(html.Div(
                        [
                            dbc.Button("?", id="info-sentiment", outline=True,
                                       className="info-button ml-0", size="sm"),
                            dbc.Tooltip(
                                "A number in percentage represents the attitude or the feeling of the tweet."
                                "It is classified into positive sentiment and negative sentiment. "
                                "(i.e. the tweet has more positive sentiment as the number goes higher "
                                "and vice versa.)",
                                target="info-sentiment",
                                placement="top-start",
                                id="tooltip-sentiment",
                                style={'font-size': '16px'}
                            )
                        ], className="info-div"
                    ), className="info-col")
                ], className="feature-row"),
                dbc.Row([
                    dbc.Col(
                        html.Div('Hate Speech', className="feature ml-0", style={'background-color': '#778487'})),
                    dbc.Col(html.Div(
                        [
                            dbc.Button("?", id="info-hate", outline=True,
                                       className="info-button ml-0", size="sm"),
                            dbc.Tooltip(
                                "A number in percentage represents how much the tweet expresses hate, profanity, "
                                "or offensive language towards a person or group based on race, religion, sex, "
                                "or sexual orientation.",
                                target="info-hate",
                                placement="top-start",
                                id="tooltip-hate",
                                style={'font-size': '16px'}
                            )
                        ], className="info-div"
                    ), className="info-col")
                ], className="feature-row"),
                dbc.Row([
                    dbc.Col(
                        html.Div('Subjectivity', className="feature ml-0", style={'background-color': '#17a2b8'})),
                    dbc.Col(html.Div(
                        [
                            dbc.Button("?", id="info-subjectivity", outline=True,
                                       className="info-button ml-0", size="sm"),
                            dbc.Tooltip(
                                "A number in percentage represents how much the tweet is colored by the viewpoint "
                                "of the tweet's author.",
                                target="info-subjectivity",
                                placement="top-start",
                                id="tooltip-subjectivity",
                                style={'font-size': '16px'}
                            )
                        ], className="info-div"
                    ), className="info-col")
                ], className="feature-row")
            ]

            progress = [
                dbc.Progress(f"{content['Sentiment']} %", value=content['Sentiment'], color="rgb(220, 53, 69)",
                             className="mb-3 progress-item"),
                dbc.Progress(f"{content['Hate Speech']} %", value=content['Hate Speech'], color="#778487",
                             className="mb-3 progress-item"),
                dbc.Progress(f"{content['Subjectivity']} %", value=content['Subjectivity'], color="rgb(23, 162, 184)",
                             className="progress-item")
            ]

            knn_heading = "You can get similar tweets according to one of the following categories:"


            knn_form = dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "User Characteristics", "value": 1},
                                    {"label": "Tweet Characteristics", "value": 2},
                                    {"label": "NLP Features", "value": 3}
                                ],
                                value=1,
                                id="radios",
                                inline=True,
                                labelStyle={'font-size': '20px', "margin-right": "40px"},
                                custom=False,
                                inputStyle={"margin-right": "10px"}
                            )
                        ),
                        dbc.Col(
                            dbc.Button("Get Similar Tweets", color="primary", size="lg", id="knn-button"),
                            width='auto', className="mr-0"
                        ),
                        dbc.Col(html.Div(
                                [
                                    dbc.Button("?", id="knn-info-btn", outline=True, className="ml-0", size="sm"),
                                    dbc.Tooltip(
                                        "By choosing one of the 3 options and clicking the button, you will be provided "
                                        "by 10 tweets from our database that have the most characteristic similarities "
                                        "to your analyzed tweet. The tweets will be plotted on a graph according to "
                                        "similarity distances. i.e. The closer the point is to the center, the more it resembles "
                                        "the analyzed tweet's chosen characteristics",
                                        target="knn-info-btn",
                                        placement="top-start",
                                        id="tooltip-tweet-char",
                                        style={'font-size': '16px'}
                                    )
                                ], id="knn-info-div"), width='auto', id="knn-info-col")
                    ], align="center", id="knn-form", className="p-3 my-4"
                )

            graph_row = dbc.Row([
                dbc.Col(dcc.Loading(html.Div(id="graph-container", className="mr-2")
                                    , type="dot", style={"height": "0.5rem"}), width='4'),
                dbc.Col(html.Div(id="text-container"), width='3'),
                dbc.Col(html.Div(id="table-container", className="ml-2"), width='5')
            ], className="graph-container-row")


            original_tweet = html.Div(
                html.Iframe(src="https://twitframe.com/show?url=" + content['tweetEmbed'],
                            height='100%', width='100%', className="tweet-frame"), id="tweet-frame-div", className="tables"
            )

            return original_tweet, tweet_frame_heading, user_data_table, user_table_heading, tweet_table_heading, content_data_table, \
                   features_heading, progress, features_items, knn_heading, knn_form, graph_row, is_open1
        elif id_valid != 0 or n2:
            return '', '', '', '', '', '', '', '', '', '', '', '', not is_open1
    else:
        return '', '', '', '', '', '', '', '', '', '', '', '', is_open1

# A callback function opens an embed tweet when the user clicks the profile picture.
@app.callback(
    Output('tweet-modal', 'is_open'),
    [Input("img-button", "n_clicks"), Input("tweet-close", "n_clicks")],
    [State("tweet-modal", "is_open")],
)
def open_embedded_tweet(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# A callback generates the K-NN graph when the user clicks the 'Get Similar Tweets' button.
@app.callback(
    Output('graph-container', 'children'),
    [Input('knn-button', 'n_clicks')],
    [State('radios', 'value')]
)
def draw_graphs(n_clicks, value):
    if n_clicks:
        global curve_type
        curve_type = value
        global user_char, tweet_user, content_data, tweet_content, features_data, tweet_features
        if value == 1:
            user_char = user_characteristics_datasets()
            tweet_user = get_user_char()
            r_and_theta = scale_and_knn(user_char['user_char_with_claim'],
                                        user_char['user_char_without_claim'],
                                        tweet_user['new_tweet'])
            # print(r_and_theta)
            graph = draw_graph(r_and_theta)
            graph_div = html.Div(graph, id="graph-div")

        elif value == 2:
            content_data = tweet_characteristics_datasets()
            tweet_content = get_tweet_content()
            r_and_theta = scale_and_knn(content_data['tweet_char_with_claim'],
                                        content_data['tweet_char_without_claim'],
                                        tweet_content['new_tweet'])
            # print(r_and_theta)
            graph = draw_graph(r_and_theta)
            graph_div = html.Div(graph, id="graph-div")

        elif value == 3:
            features_data = form_features_dataset()
            tweet_features = get_tweet_features()
            r_and_theta = scale_and_knn(features_data['features_with_claim'],
                                        features_data['features_without_claim'],
                                        tweet_features['new_tweet'])
            # print(r_and_theta)
            graph = draw_graph(r_and_theta)
            graph_div = html.Div(graph, id="graph-div")

        # print(tweet_user)

        return graph_div

    else:
        return ''

# A callback function generates a comparison table and a text when the user clicks a point on the K-NN graph.
@app.callback(
    [Output('table-container', 'children'),
     Output('text-container', 'children')],
    [Input('tweets-graph', 'clickData')]
)
def draw_tables(clickData):
    if(clickData):
        tweet_index = clickData['points'][0]['theta']

        if curve_type == 1:  # user characteristics
            if tweet_index == 0.5:
                table = draw_table_same(tweet_user['new_tweet_true_false'], 'User Characteristics')
                text = content['analyzed_text']
            else:
                table = draw_table(tweet_index, user_char['user_char_true_false'],
                                   tweet_user['new_tweet_true_false'], "User Characteristics")
                text = user_char['user_char'].iloc[tweet_index]['text']

        elif curve_type == 2:  # tweet characteristics
            if tweet_index == 0.5:
                table = draw_table_same(tweet_content['new_tweet_true_false'], 'Tweet Characteristics')
                text = content['analyzed_text']
            else:
                table = draw_table(tweet_index, content_data['tweet_char_true_false'],
                                   tweet_content['new_tweet_true_false'], "Tweet Characteristics")
                text = content_data['tweet_char'].iloc[tweet_index]['text']

        elif curve_type == 3: # ML features
            if tweet_index == 0.5:
                table = draw_table_same(tweet_features['new_tweet_true_false'], 'ML Features')
                text = content['analyzed_text']
            else:
                table = draw_table(tweet_index, features_data['features_true_false'],
                                   tweet_features['new_tweet_true_false'], "ML Features")
                text = features_data['features'].iloc[tweet_index]['text']

        table_div = html.Div(table, id="knn-table-div")
        text_div = html.Div([
            html.Div("Tweet's text", id="text-title-div"),
            html.Div(text, id="tweet-text-div")
        ], id="text-div")


        return table_div, text_div
    else:
        return '', ''

# A callback function alerts the user when a wrong ID or URL is entered.
@app.callback(
    Output('submit-button', 'disabled'),
    [Input('input-id', 'value')]
)
def disable_button(input_value):
    if input_value is None:
        return True
    if input_value is not None:
        return False

