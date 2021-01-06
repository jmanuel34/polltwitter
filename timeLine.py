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
# -*- coding: utf-8 -*-

""""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)

        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])

        return true

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening


if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(follow=[38744894], track=['#pythoncentral'])
def followers_count(cuenta):
    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    user = api.get_user(cuenta)
    return user.followers_count;
"""
x = tweepy.API(auth)
for tweets in x.user_timeline():
    print(tweets.created_at)
    print(tweets.text)
    print(' *'*40)

"""
stuff = api.user_timeline(screen_name = 'danieltosh', count = 100, include_rts = True)

print (stuff)
"""