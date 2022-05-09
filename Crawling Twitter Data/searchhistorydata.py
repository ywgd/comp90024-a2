
import tweepy
import json

consumer_key = "8k7SzAflvtcFmaqJsTiqzylYa"
consumer_secret = "qPqhLwP77RiuWRgLn8KKPscFLX6PQprPXtrYiaJLxH0Hpe2846"
access_token = "1517355964617297920-mOWbcyxo7Zr9SXsRN8nXIn9zrm2NpT"
access_token_secret = "zvJ7znhMV4ZmVG6fKl3t4w7e4McNUU7x8cCTGNympdwqD"

## set API connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# set wait_on_rate_limit =True; as twitter may block you from querying if it finds you exceeding some limits
api = tweepy.API(auth, wait_on_rate_limit = True)  

# exclude retweets
search_words = ["covid -filter:retweets", "coronavirus -filter:retweets"]


tweets = tweepy.Cursor(api.search_tweets, q = search_words,
                       # geocode = "-37.840935, 144.946457, 40km",
                       lang = "en", result_type = "popular").items(10)
                       # max_id = 1523663926558289920
## the geocode is for India; format for geocode="lattitude,longitude,radius"
## radius should be in miles or km


for tweet in tweets:
    # if (tweet.user.location == "Melbourne, Australia"):
    print("created_at: {}\nid: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
            format(tweet.created_at, tweet.id, tweet.user.screen_name, tweet.text, tweet.user.location))
    print("\n")
# tweet.user.location will give you the general location of the user and not the particular location for the tweet itself, as it turns out, most of the users do not share the exact location of the tweet


'''
# only for academic access
import tweepy as tw

bearer_token = "AAAAAAAAAAAAAAAAAAAAACAQbwEAAAAAMMc5leYe2RxXTUO4xNKAhSp9DuI%3D3AI6uRezA6X1teJIzd0WYMh53nIjyE421lYPj4o9RPJNmEeRgY"
client = tw.Client(bearer_token)

query = 'covid -is:retweet'
end_time = '2022-05-02T16:46:00Z'

# print("-----------------------------------------------")
response = client.search_recent_tweets(query = query, tweet_fields=['context_annotations', 'created_at', 'geo'], place_fields=['place_type', 'geo'], expansions='geo.place_id', end_time = end_time)
print("-----------------------------------------------")
places = {p["id"]: p for p in response.includes['places']}
# print(response.meta)
# print("-----------------------------------------------")

tweets = response.data
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)
    # print(tweet.location)
    # if tweet.geo != None:
        # print(tweet.text.encode('utf-8', errors='ignore'))

    if places[tweet.geo['place_id']]:
        place = places[tweet.geo['place_id']]
        print(place.full_name)
'''

'''
import sys
import os
import re
import tweepy
import pandas as pd
from tweepy import OAuthHandler
# from textblob import TextBlob

consumer_key = "8k7SzAflvtcFmaqJsTiqzylYa"
consumer_secret = "qPqhLwP77RiuWRgLn8KKPscFLX6PQprPXtrYiaJLxH0Hpe2846"
# access_token = "1517355964617297920-mOWbcyxo7Zr9SXsRN8nXIn9zrm2NpT"
# access_token_secret = "zvJ7znhMV4ZmVG6fKl3t4w7e4McNUU7x8cCTGNympdwqD"

#obtaining tweets within a certain distance from a specific location, and converting important attributes into a dataframe
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)
if not api:
    print("Can't Authenticate")
    sys.exit(-1)

tweet_lst = []
geoc = "-37.840935, 144.946457, 1000km"
query = ["covid"]
for tweet in tweepy.Cursor(api.search_tweets, geocode = geoc, q = query).items(10):
    tweetDate = tweet.created_at.date()
    if tweet.coordinates != None:
        tweet_lst.append([tweetDate,tweet.id,tweet.coordinates["coordinates"][0],
                tweet.coordinates["coordinates"][1],
                tweet.user.screen_name,
                tweet.user.name, tweet.text,
                tweet.user._json["geo_enabled"]])
tweet_df = pd.DataFrame(tweet_lst, columns=['tweet_dt', 'id', 'lat','long','username', 'name', 'tweet','geo'])
'''
