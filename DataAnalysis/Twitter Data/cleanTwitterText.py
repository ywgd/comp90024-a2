def cleanText(raw_tweets):
    import re
    import string
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    stopwords = stopwords.words('english') # result is list

    raw_text = raw_tweets['text']

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
    raw_tweets['splitwords'] = words

    words_string = " ".join(map(str, words))
    raw_tweets['splitwords'] = words_string

    return raw_tweets
