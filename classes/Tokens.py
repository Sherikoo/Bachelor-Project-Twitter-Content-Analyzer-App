import tweepy
from datetime import date

# Implementing the Singleton pattern.
class T (object):

    # Initializations
    followers = 0
    following = 0
    name = 0
    api = 0
    text = 0
    hash = 0
    created_at = 0
    descr = 0
    verified = 0
    tweets = 0
    userAge = 0
    avgPerDay = 0
    img = 0
    favorite_count = 0
    id = 0
    favorite_count_knn = 0
    followers_knn = 0
    following_knn = 0
    user_listed_count_knn = 0
    user_favourites_count = 0
    user_mentions_count = 0

    # Authentication credentials
    API_key="9vT6YSRldTWRxIqRQz1v7vMp2"
    API_secret="PXYLVKuldsPeGZ2gF1AkieQ1AG0uaqoVpFwEvBN9vchSLaYk02"
    Token_key="1173359684134326277-Ppx95QT5Qx5nNH7cfypX7QiNUcKdFV"
    Token_secret="VvVLi3eJobKgon3H5G9h2mzohZkfnhDacDKTo7Tm8r6uE"
    Bearer_Token='AAAAAAAAAAAAAAAAAAAAADTdLQEAAAAAmTSfCS7CxR0ZqFaC4ILo809csQc%3DxoWhK17zcSRl0HPy20t32R5XNfnuezX4w7dHvjM1QZSO7ktKlO'

    # Authenticate the API calls and access the Twitter API
    auth = tweepy.OAuthHandler(API_key, API_secret)
    auth.set_access_token(Token_key, Token_secret)

    # Get all tweet's data from the Twitter API
    def get_tweet_object(self):
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        try:
            saving_tw_id = self.api.get_status(self.id, tweet_mode='extended')
            self.followers_knn = saving_tw_id.user.followers_count
            if saving_tw_id.user.followers_count > 10000:
                self.followers = saving_tw_id.user.followers_count/1000
                self.followers = (str(self.followers)[:4])+'k'
            else:
                self.followers = saving_tw_id.user.followers_count
            self.following_knn = saving_tw_id.user.friends_count
            if saving_tw_id.user.friends_count >10000 :
                self.following = saving_tw_id.user.friends_count/1000
                self.following = (str(self.following)[:4])+'k'
            else:
                self.following = saving_tw_id.user.friends_count

            self.name = saving_tw_id.user.screen_name
            self.hash = saving_tw_id.entities['hashtags']
            self.text = saving_tw_id.full_text
            self.created_at = saving_tw_id.user.created_at
            self.descr = saving_tw_id.user.description
            self.verified = saving_tw_id.user.verified
            self.tweets = saving_tw_id.user.statuses_count
            today = date.today()
            age = today - self.created_at.date()
            self.userAge = age.days
            self.avgPerDay = round(self.tweets / self.userAge, 2)
            self.img = saving_tw_id.user.profile_image_url_https
            self.user_listed_count_knn = saving_tw_id.user.listed_count
            self.favorite_count_knn = saving_tw_id.favorite_count
            self.user_favourites_count = saving_tw_id.user.favourites_count
            self.user_mentions_count = len(saving_tw_id.entities['user_mentions'])
            if saving_tw_id.favorite_count > 1000000:
                self.favorite_count = saving_tw_id.favorite_count/1000000
                self.favorite_count = (str(self.favorite_count)[:3])+'M'
            elif saving_tw_id.favorite_count > 100000:
                self.favorite_count = saving_tw_id.favorite_count/1000
                self.favorite_count = (str(self.favorite_count)[:5])+'k'
            elif saving_tw_id.favorite_count > 10000:
                self.favorite_count = saving_tw_id.favorite_count/1000
                self.favorite_count = (str(self.favorite_count)[:4])+'k'
            elif saving_tw_id.favorite_count > 1000:
                self.favorite_count = saving_tw_id.favorite_count/1000
                self.favorite_count = (str(self.favorite_count)[:3])+'k'
            else :
                self.favorite_count = saving_tw_id.favorite_count

            return 0
        except:
            return 1

    # A function the used to embed a tweet in the App.
    def getEmbedTweet(self):

        try:
            URL='https://twitter.com/'+self.name+'/status/'+self.id
            return self.api.get_oembed(url=URL, maxwidth='550',
                                       hide_thread='true', align='center', theme='dark')['url']
        except:
            return 'Can not get tweet source!'

