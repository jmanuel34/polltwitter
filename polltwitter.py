#import codecs
import time
import tweepy
#import json
import requests
import mysql.connector
from mysql.connector import errorcode
import sys
import MySqlconn
""" Parámetros de conexion """
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'twitter',
    'port': '8889'
#    ,'raise_on_warnings': True
}
fichero_cuentas = "CuentasTest.json"
last_tweet= '1189642406729265152'
fichero_claves = './claves.txt'


def twitter_connect():
    with codecs.open(fichero_claves, 'r', encoding = 'utf-8') as fp:
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
            return (api)
        except:
            print("Error during authentication")

def followers_count(cuenta):
#    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    api = twitter_connect()
    user = api.get_user(cuenta)
    return user.followers_count;




"""
    obj = MySqlconn()
    result = obj.mysqlConnect(config)
    if result:
    # ejeplo 1 - INSERT
        print(obj.prepare("INSERT INTO personas (nombre, edad, genero) VALUES ('Josefina4', 244, 'Mujer');"))
        obj.prepare("INSERT INTO personas (nombre, edad, genero) VALUES ('Josefina5', 245, 'Mujer');")
"""

def insertarTweet(dict):
    sqlTweet = ("INSERT INTO tblTweet" +
                 + "( tema, fecha, texto, textoLargo, id_twett, localizacion, coordenadas)" +
                 + " VALUES (dict['Screen Name'], dict['User Name'], dict['Twett Id']" +
                 + " dict['Twett Id'];)")



def getTweet(cuenta, limit, last_tweet):
    api = twitter_connect()
    user= api.get_user(cuenta)
    try:
        tweetsObj = tweepy.Cursor( \
            api.user_timeline, \
            user_id=user.id, \
            exclude_replies=True, \
            tweet_mode='extended', \
            since_id = last_tweet
            ).items(limit)
        for cnt, tweet in enumerate(tweetsObj):
            dict= {
                'user_id': user.id,
                'screen_Name': tweet.user.screen_name,
                'user_name': tweet.user.name,
                'user_location': tweet.user.location,
                'tweet_text': tweet.full_text,
                'tweet_coordinates': tweet.coordinates,
                'twett_id': tweet.id,
            }
        return (dict)
    except tweepy.error.TweepError as et:
        print(et)


def getId(cuenta):
    api = twitter_connect()
    user = api.get_user(cuenta)
    return user.id
    """
    api = twitter_connect()
    user= api.get_user(cuenta).id

    tweets = []
    try:
        tweetsObj = tweepy.Cursor( \
            api.user_timeline, \
            user_id=user.id, \
            exclude_replies=True, \
            tweet_mode='extended', \
            since_id = last_tweet
            ).items(limit)
        for cnt, tweet in enumerate(tweetsObj):
            dict= {
                'User Id': tweet.author.id,
            }
            user_id = (dict['User Id'])

    except tweepy.error.TweepError as et:
        print(et)

    return user_id
"""
def insertarCuenta(dict):
#    con = getConnect()
    obj= MySqlconn()
    result = obj.mysqlConnect(config)
    if result():
        obj.prepare("INSERT INTO tblCuentaTw (screen_name, user_name) VALUES ('@Josefina4', 'josefina');")
    screenName= dict['Screen Name']
    userName = dict['User Name']
    web = dict['Web']
    facebook = dict['Facebook']
#    tweetObj = dict['Object']

with open(fichero_cuentas,"r") as cuentas_twitter:
    data_in = json.load(cuentas_twitter)
    data_out = {}
    data_out ['cuentas'] =[]
    file_out = time.strftime("%Y%m%d-%H%M%S")
    #    fileOut = time.strftime("%Y%m%d")

    for p in data_in['cuentas']:
        if (p['twitter'] != ''):
            try:
                cuenta = {}
                cuenta["user_id"] = getId(p['twitter'])
                cuenta["twitter"] = p['twitter']
                datos_tweet = getTweet(p['twitter'], 1, last_tweet)

                cuenta['screen_name'] = str(datos_tweet['screen_Name'])
                cuenta['user_name'] = str(datos_tweet['user_name'])
                cuenta['tweet_text'] = str(datos_tweet['tweet_text'])
                cuenta['tweet_coordinates'] = str(datos_tweet['tweet_coordinates'])
                cuenta['twett_id'] = str(datos_tweet['twett_id'])

                cuenta['seguidores'] = (str(followers_count(p['twitter'])))
                cuenta['last_tweet'] = str(datos_tweet['twett_id'])
#                cuenta['Tweet Id'] = '1189642406729265152'
#                result = insertarCuenta(cuenta)
#                insertarCuenta(cuenta)
                data_out['cuentas'].append(cuenta)
 #               print (cuenta)
            except:
                print ("Error de nombre de cuenta "+ p['twitter'])

    with open("cuentas_file"+file_out+".json", "w") as result_file:
        json.dump(data_out, result_file, indent=2, sort_keys=True, ensure_ascii=False)


#file_users = 'CandidatosElectos-2019-04.csv'



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
"""
def getConnect():
    config = {
        'user': 'jm',
        'password': 'Recuerd0la1',
        'host': '127.0.0.1',
        'port': '8889',
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



"user_mentions": [{
    "screen_name": "TwitterEng",
    "name": "Twitter Engineering",
    "id": 6844292,
    "id_str": "6844292",
    "indices": [81, 92]
}, {

def getTweets(cuenta, limit, last_tweet):
    api = twitter_connect()
    user= api.get_user(cuenta)
    try:
        tweetsObj = tweepy.Cursor( \
            api.user_timeline, \
            user_id=user.id, \
            exclude_replies=True, \
            tweet_mode='extended', \
            since_id = last_tweet
            ).items(limit)
        for cnt, tweet in enumerate(tweetsObj):
#            if not cnt < limit:
#                break
#            else:
            dict= {
                'user_id': tweet.id,
                'screen_name': tweet.user.screen_name,
                'user_name': tweet.user.name,
                'user_location': tweet.user.location,
                'tweet_text': tweet.full_text,
                'tweet_coordinates': tweet.coordinates,
                'twett_id': tweet.id,
                'web': "",
                'facebook': "",
                'object': tweetsObj.current_page
#                'Twett Number': tweet.since_id
            }
            insertarTweet(dict)
#            print(tweet.text.replace("\n", ""))
#            print ("Since ID = 1189642406729265152")
#            print (dict)
#            tweets.append(dict)
#            last_tweet_id = (dict['Tweet Id'])
    except tweepy.error.TweepError as et:
        print(et)
"""
