import re
import json
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#pip install --user -U nltk
#python -m nltk.downloader popular

stopwords = stopwords.words('english') # result is list

#print(type(stopwords))
#print(string.punctuation) # string

with open('twitterdata_with_text.json','r',encoding="utf-8") as f:
    raw_tweets = json.load(f)


# reference: https://machinelearningmastery.com/clean-text-machine-learning-python/
for i in range(len(raw_tweets)):
    #raw_tweets[i]: dict
    
    #print(raw_tweets[i]['text'])
    raw_text = raw_tweets[i]['text']

    # remove "http"
    raw_text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", raw_text) 
    raw_text = " ".join(raw_text.split())

    # remove "&amp"
    raw_text = raw_text.replace("&amp", "")

    # split into words
    tokens = word_tokenize(raw_text)

    # covert to lower case
    tokens = [w.lower() for w in tokens]

    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # reference for isascii(): https://note.nkmk.me/en/python-str-num-determine/
    # remove remaining tokens that are not ASCII
    words = [word for word in stripped if word.isascii()]

    words = [w for w in words if not w in stopwords]
    raw_tweets[i]['splitwords'] = words
        
    #words_string = " ".join(map(str, words))
    #raw_tweets[i]['splitwords'] = words_string


