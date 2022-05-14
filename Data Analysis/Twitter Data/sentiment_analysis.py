import re
import json
from textblob import TextBlob

# tweet is the file we get after cleaning (cleanTwitterText.py)
def tweet_sentiment(tweet):

        # create TextBlob object of passed tweet text
        twitter_data = TextBlob(tweet)

        # set sentiment
        if twitter_data.sentiment.polarity > 0:
            return 'positive'
        elif twitter_data.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

if __name__ == "__main__":

    with open('twitterdata_with_text.json','r',encoding="utf-8") as f:
        Twitter = json.load(f)

    tweets = []
    for item in Twitter:
        # create a dictionary to store sentiment regard to the tweet.text (a new field in json)
        sentiment_tweet = {}
        sentiment_tweet['text'] = item["text"]
        sentiment_tweet['sentiment'] = tweet_sentiment(item["text"])

        # print(parsed_tweet)
        # print("===============================================================")

        # appending sentiment_tweet to tweets list for calculating
        tweets.append(sentiment_tweet)


    # print(len(tweets))

    # positive tweets
    positive_tweet = []
    for tweet in tweets:
        if tweet['sentiment'] == 'positive':
            positive_tweet.append(tweet['sentiment'])
    positive_per = round((len(positive_tweet)/len(tweets)) * 100, 4)
    print("Positive tweets percentage: {} %".format(positive_per))
    
    negative_tweet = []
    for tweet in tweets:
        if tweet['sentiment'] == 'negative':
            negative_tweet.append(tweet['sentiment'])
    negative_per = round((len(negative_tweet)/len(tweets)) * 100, 4)
    print("Negative tweets percentage: {} %".format(negative_per))
    
    neutral_per = round(100 - positive_per - negative_per, 4)
    print("Neutral tweets percentage: {} %".format(neutral_per))
