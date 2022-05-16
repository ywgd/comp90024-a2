import json
from cleanTwitterText import cleanText

with open('twitterdata_extended_done_comma.json', 'r', encoding="utf-8") as f:
    raw_tweets = json.load(f)
# print(len(raw_tweets))

# remove duplicate tweets
raw_tweets = {each['id']: each for each in raw_tweets }.values()
# print(len(raw_tweets))

with open('final_twitter_data.json', 'a', encoding='utf-8') as f:
    for item in raw_tweets:
        # search data has a different field name than stream data, rename it
        if "full_text" in item:
            item['text'] = item.pop("full_text")
        item = cleanText(item)
        json.dump(item, f)
        f.write(",")
        f.write('\n')
