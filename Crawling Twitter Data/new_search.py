import tweepy
import json

consumer_key = "8k7SzAflvtcFmaqJsTiqzylYa"
consumer_secret = "qPqhLwP77RiuWRgLn8KKPscFLX6PQprPXtrYiaJLxH0Hpe2846"
access_token = "1517355964617297920-mOWbcyxo7Zr9SXsRN8nXIn9zrm2NpT"
access_token_secret = "zvJ7znhMV4ZmVG6fKl3t4w7e4McNUU7x8cCTGNympdwqD"

# set API connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# set wait_on_rate_limit =True; as twitter may block you from querying if it finds you exceeding some limits
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = tweepy.Cursor(api.search_tweets,
                       q="covid OR coronavirus geocode:-37.840935,144.946457,40km -filter:retweets AND -filter:quote",
                       lang="en").items(10000)

# the geocode is for melbourne; format for geocode="latitude,longitude,radius"
# radius should be in km/mi


for tweet in tweets:
    with open('recent_tweet_comma.json', 'a', encoding='utf-8') as tf:
        tf.write('\n')
        json.dump(tweet._json, tf)
        tf.write(',')
        
        
"""
for tweet in tweets:
    with open('recent_tweet_comma.json', 'a', encoding='utf-8') as tf:

        has_text = True
        if "text" not in tweet._json:
            has_text = False

        if has_text:
            if "extended_tweet" in tweet._json:
                print(tweet._json['text'])
                print("================================")
                temp_text = tweet._json['extended_tweet']['full_text']
                tweet._json['text'] = temp_text
                print(tweet._json['text'])
            else:
                print("No extended text")

            tf.write('\n')
            json.dump(tweet._json, tf)
            tf.write(',')

"""
