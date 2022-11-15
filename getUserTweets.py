import tweepy
import configparser
import pandas as pd
import datetime
import sys

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
userID = sys.argv[1]
output_file_name = sys.argv[2]

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client = tweepy.Client(
    consumer_key = api_key,
    consumer_secret = api_key_secret,
    access_token = access_token,
    access_token_secret = access_token_secret
)

user = api.get_user(screen_name=userID)

f = open(output_file_name, "w")

class Tweet:
    def __init__(self, id, date, text):
        self.date = date
        self.text = text
        self.id = id

stack = []

tweets = api.user_timeline(screen_name=userID, count=20000, include_rts = True, tweet_mode = 'extended')
i = 0
id=0
for info in tweets[:]:
    i+=1
    id=int("{}".format(info.id))
    date=info.created_at
    insertion_date = datetime.datetime(date.year, date.month, date.day)
    current_datetime = datetime.datetime.now()
    if current_datetime - insertion_date > pd.Timedelta("7 days"):
        stack.append(Tweet(id, date, info.full_text))        
x=1
while(x>0):
    x=-1
    tweets = api.user_timeline(screen_name=userID, count=20000, max_id = id, include_rts = True, tweet_mode = 'extended')
    id=0
    for info in tweets[:]:
        x+=1
        id=int("{}".format(info.id))
        date=info.created_at
        insertion_date = datetime.datetime(date.year, date.month, date.day)
        current_datetime = datetime.datetime.now()
        if current_datetime - insertion_date > pd.Timedelta("7 days"):
            stack.append(Tweet(id, date, info.full_text)) 
while(len(stack)>0):
    t=stack.pop()
    f.write(t.date.strftime("%m/%d/%Y, %H:%M:%S"))
    f.write('\n')
    f.write(t.text)
    f.write('\n')
    f.write('\n')
