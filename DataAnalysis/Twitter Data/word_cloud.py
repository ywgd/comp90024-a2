import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


with open('twitterdata_with_text.json', 'r', encoding="utf-8") as f:
        raw_tweets = json.load(f)

for i in range(len(raw_tweets)):
    text = raw_tweets[i]['splitwords']

# create stopword list
stopwords = set(STOPWORDS)
stopwords.update(["covid"])

# generate
wordcloud = WordCloud(collocations = False, background_color = 'white', stopwords = stopwords, max_words=1000000).generate(text)

# show
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show() 