# import tweepy
# import configparser

import couchdb
import json
# import socket


# read configs
# config = configparser.RawConfigParser()
# config.read("config.ini")

'''
api_key = config['twitter']['consumer_key']
api_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']



# authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
'''

# socket.getaddrinfo("172.26.134.18", 8080)

# couchdb
couch = couchdb.Server("http://admin:admin@172.26.134.18:5984/")

# db = couch.create("twitter_data")
db = couch["twitter_data"]
print("Database Successfully Created.");  

# print("ok")
# public_tweets = api.home_timeline()

with open("twitterdata_extended_done_comma.json", "r", encoding = "utf-8") as f:
    Twitter = json.load(f)

# remove duplicate tweets
Twitter = {each['id']: each for each in Twitter }.values()

for item in Twitter:
    # search data has a different field name than stream data, rename it
    if "full_text" in item:
        item['text'] = item.pop("full_text")
    print(item['text'])
    # print()
    # jsonStr = '{' + '"username":' + '"' + tweet.user.screen_name + '"' + ',"tweet":' + '"' + tweet.text + '"' + '}'
    
    db_entry = json.loads(item)
    db.save(db_entry)
    # dic = {"user": item["id"], "tweet":item['text']}
    # db.save(dic)
