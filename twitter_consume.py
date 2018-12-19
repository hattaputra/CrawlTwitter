import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "Fz2TC10tUiL4xB3oYOoca0eD4"
        consumer_secret = "B3TKlgIjgYDfz1AW7vbC1hYVuHq55RQ8aNQFd4zs8M3HcJgMnM"
        access_token = "1074527011949826048-DgZlg9Hz7TWJYVJ6PRXaysoB4G5lwN"
        access_secret = "9376Qy5M6o815QEzUmxGi3dU3edVBHW5pWryplD0XFNrz"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client
