import tweepy
import configparser
import couchdb
import json

# read configs
config = configparser.RawConfigParser()
config.read("config.ini")

api_key = config['twitter']['consumer_key']
api_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']


# authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# couchdb
couch = couchdb.Server('http://admin:123456@127.0.0.1:5984/')


db = couch['test']

# print("ok")
public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)
    print()
    # jsonStr = '{' + '"username":' + '"' + tweet.user.screen_name + '"' + ',"tweet":' + '"' + tweet.text + '"' + '}'
    dic = {'user':tweet.user.screen_name, 'tweet':tweet.text}
    db.save(dic)


