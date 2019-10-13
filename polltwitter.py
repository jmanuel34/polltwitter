import codecs
import time

import tweepy
import json
filepath = './claves.txt'
with codecs.open(filepath, 'r', encoding = 'utf-8') as fp:
    consumer_key = fp.readline()
    print("prueba"+consumer_key+"Final")
    consumer_key = consumer_key.replace('\n', '')
    print("prueba" + consumer_key + "Finalde todo")
    consumer_secret = fp.readline()
    consumer_secret = consumer_secret.replace('\n', '')
    access_token = fp.readline()
    access_token = access_token.replace('\n', '')
    access_token_secret = fp.readline()
    access_token_secret = access_token_secret.replace('\n', '')

print ("Consumer_key" + consumer_key+"Fin")
print ("Consumer_secret"+ consumer_secret+"Fin")
print("Access_token" + access_token+"Fin")
print("access_token_secret" +access_token_secret+"Fin")

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

file_users = 'CandidatosElectos-2019-04.csv'
with open("results.json","r") as results_file:
    data = json.load(results_file)
    fileOut = time.strftime("%Y%m%d-%H%M%S")
#    with open(fileOut, 'w') as outfile:
#        json.dump(data, outfile)
    for p in data['cuenta']:

        print ("Nombre "+ p['nombre'])
        print ("twitter " + p['twitter'])
        if (p['twitter'] != ''):
            print("Nombre: "+ str(followers_count(p['twitter'])))
