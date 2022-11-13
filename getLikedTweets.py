import tweepy
import configparser
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
client_id = config['twitter']['client_id']
client_secret = config['twitter']['client_secret']
userID = config['twitter']['username']
output_file_name = config['twitter']['output_file_name']

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
client = tweepy.Client('BEARER TOKEN HERE')
f = open(output_file_name, "w")

user = api.get_user(screen_name=userID)
tweets = client.get_liked_tweets(user.id)
for tweet in tweets.data:
    f.write(tweet.text)
    f.write('\n')

token=tweets.meta['next_token']
while token:
    tweets = client.get_liked_tweets(user.id, pagination_token=token)
    for tweet in tweets.data:
        f.write(tweet.text)
        f.write('\n')
    token = tweets.meta['next_token']