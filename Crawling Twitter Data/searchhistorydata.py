import tweepy

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
                       lang="en").items(10)

# the geocode is for melbourne; format for geocode="latitude,longitude,radius"
# radius should be in km/mi

for tweet in tweets:
    print("created_at: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
          format(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location))
    print("\n")
