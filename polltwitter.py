import codecs
import time
import tweepy
import json
#import sqlite3 as lite
import mysql.connector
from mysql.connector import errorcode

import sys

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
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def followers_count(cuenta):
#    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    user = api.get_user(cuenta)
    return user.followers_count;

def getTweets(cuenta, limit):
    user= api.get_user(cuenta)
    tweets = []
    try:
        tweetsObj = tweepy.Cursor( \
            api.user_timeline, \
            user_id=user.id, \
            exclude_replies=True, \
            tweet_mode='extended', \
            since_id = '1189642406729265152'
            ).items(limit)
        for cnt, tweet in enumerate(tweetsObj):
#            if not cnt < limit:
#                break
#            else:
            dict= {
                'Screen Name': tweet.user.screen_name,
                'User Name': tweet.user.name,
                'User Location': tweet.user.location,
                'Tweet Text': tweet.full_text,
                'Tweet Coordinates': tweet.coordinates,
                'Twett Id': tweet.id_str
#               'Twett Number: tweet.since_id'
            }
            # print(tweet.text.replace("\n", ""))
            tweets.append(dict)
    except tweepy.error.TweepError as et:
        print(et)
    return tweets

    return tweets
def getConnect():
    config = {
        'user': 'jm',
    'password': 'Recuerd0la1',
    'host': '127.0.0.1',
    'database': 'twitter',
    'raise_on_warnings': True
    }
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o password invalidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de datos inexistente")
        else:
            print(err)
    else:
        cnx.close()
#file_users = 'CandidatosElectos-2019-04.csv'

def recordb(sql):
    try:
#        con = getconnect()
        con = getConnect()
        cur = con.cursor()
        cur.execute( 'CREATE TABLE IF NOT EXIST tweet (Id INT PRIMARY KEY, tema TEXT, fecha DATE, text TEXT, message BLOB)')
        cur.execute (sql)
        data = cur.fetchone()[0]
        print("SQLite version: {}".format(data))
    except con.Error as e:
        if con:
            con.rollback()
        print
        "Error {}:".format(e.args[0])
        sys.exit(1)
    finally:
        con.close()

with open("CuentasTest.json","r") as results_file:
    data = json.load(results_file)
    seguidores = {}
    seguidores ['cuentas'] =[]
    fileOut = time.strftime("%Y%m%d-%H%M%S")
    #    fileOut = time.strftime("%Y%m%d")

    for p in data['cuentas']:
        if (p['twitter'] != ''):
            try:
                cuenta = {}
                cuenta["twitter"] = p['twitter']
                cuenta['seguidores'] =  (str(followers_count(p['twitter'])))
                print("Seguidores: " + str(followers_count(p['twitter'])))
                cuenta['twetts'] = getTweets(p['twitter'], 1)
                cuenta['Tweet Id'] = '1189642406729265152'
                seguidores['cuentas'].append(cuenta)
                sql = ('INSERT INTO tweet (tema, fecha, text, message) VALUES ("a",time.strftime("%Y%m%d-%H%M%S"),"c","d")')
                recordb(sql)
            except:
                print ("Error de nombre de cuenta "+ p['twitter'])

    with open("seguidores"+fileOut+".json", "w") as results_file:
        json.dump(seguidores, results_file, indent=4, sort_keys=True, ensure_ascii=False)
"""
'Twett Id': '1189642406729265152'}
def retrieve_twetts(cuenta, quantity):
    twetts= {}
    for status in tweepy.Cursor(api.user_timeline(cuenta)).items(4):
        dict_ = {'Screen Name': status.user.screen_name,
                 'User Name': status.user.name,
                 'Tweet Created At': unicode(status.created_at),
                 'Tweet Text': status.text,
                 'User Location': unicode(status.user.location),
                 'Tweet Coordinates': unicode(status.coordinates),
                 'Retweet Count': unicode(status.retweet_count),
                 'Retweeted': unicode(status.retweeted),
                 'Phone Type': unicode(status.source),
                 'Favorite Count': unicode(status.favorite_count),
                 'Favorited': unicode(status.favorited),
                 'Replied': unicode(status.in_reply_to_status_id_str)
                 }
        listOfTweets.append(dict_)
    return listOfTweets
"""

"""
def retrieve_twetts(cuenta, quantity):
    twetts={}
    user = api.get_user(cuenta)
    stuff = api.user_timeline(user_id=cuenta, count=quantity, include_rts=True)
    for message in stuff:
        twetts['twett']=message.text
        print (message.text)
        twetts.append(message)
    return twetts
"""