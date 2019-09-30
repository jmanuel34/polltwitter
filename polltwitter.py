import tweepy
import codecs

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

print ("Consumer_key" + consumer_key+"Fin")
print ("Consumer_secret"+ consumer_secret+"Fin")
print("Access_token" + access_token+"Fin")
print("access_token_secret" +access_token_secret+"Fin")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

file_users = 'usuarios.txt'
with open (file_users) as fu:
    user_search = fu.readline()

api = tweepy.API(auth)
def followers_count():
#    user_search = input("Introduce el usuario del cuál quieres saber el número de seguidores: ")
    user = api.get_user(user_search)
    return user.followers_count;
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

print(" ")
print (followers_count())