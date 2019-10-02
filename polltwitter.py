import tweepy
import codecs

filepath = './claves.txt'
with codecs.open(filepath, 'r', encoding = 'utf-8') as fp:
    consumer_key = fp.readline()
    consumer_key = consumer_key.replace('\r\n', '')
    consumer_secret = fp.readline()
    consumer_secret = consumer_secret.replace('\r\n', '')
    access_token = fp.readline()
    access_token = access_token.replace('\r\n', '')
    access_token_secret = fp.readline()
    access_token_secret = access_token_secret.replace('\r\n', '')

print ("Consumer_key" + consumer_key+"Fin")
print ("Consumer_secret"+ consumer_secret+"Fin")
print("Access_token" + access_token+"Fin")
print("access_token_secret" +access_token_secret+"Fin")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

file_users = 'usuarios.txt'
users = []

with open (file_users) as fu:
#        user_search = fu.readline()
    linea = fu.readline()
    while (linea !=""):
        users.append(linea)
        linea = fu.readline()
        print (linea)
    fu.close()

print (users)

"""
def followers_count():
#    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    user = api.get_user(users[i])
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