import codecs
import time

import tweepy
import json

from tweepy import StreamListener, Stream

filepath = './claves.txt'
with codecs.open(filepath, 'r', encoding = 'utf-8') as fp:
    consumer_key = fp.readline()
    consumer_key = consumer_key.replace('\n', '')
    consumer_secret = fp.readline()
    consumer_secret = consumer_secret.replace('\n', '')
    access_token = fp.readline()
    access_token = access_token.replace('\n', '')
    access_token_secret = fp.readline()
    access_token_secret = access_token_secret.replace('\n', '')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
cuenta = 'danieltosh'

stuff = api.user_timeline(screen_name = cuenta, count = 4, include_rts = True)
for message in stuff:
    print (message.text)

"""
x = tweepy.API(auth)
for tweets in x.user_timeline():
    print(tweets.created_at)
    print(tweets.text)
    print(' *'*40)
"""