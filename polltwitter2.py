import codecs
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
print(" ")

def followers_count(cuenta):
#    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    user = api.get_user(cuenta)
    return user.followers_count;

with open("results.json", "r") as json_file:
    data = json.load(json_file)
    for p in data['cuenta']:
        user = api.get_uset(p['twitter'])
        print ("Nombre: "+ p['twitter'])
        print ("Seguidores de Twitter:" + followers_count(p['twitter']))
    json_file.close()

"""
def followers_count():
#    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    user = api.get_user("@psoe")
    return user.followers_count;

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
print(" ")
print (followers_count())
"""