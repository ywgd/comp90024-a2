import couchdb
import json
from cleanTwitterText import cleanText

couch = couchdb.Server("http://admin:admin@172.26.134.18:5984/")

dbname = "twitter_data"
if dbname in couch:
    db = couch["twitter_data"]
else:
    db = couch.create("twitter_data")
    
print("Database Successfully Created.");  


with open("twitterdata_extended_done_comma.json", "r", encoding = "utf-8") as f:
    Twitter = json.load(f)

# remove duplicate tweets
Twitter = {each['id']: each for each in Twitter }.values()

for item in Twitter:
    # search data has a different field name than stream data, rename it
    if "full_text" in item:
        item['text'] = item.pop("full_text")
    # print(item['text'])
    item = cleanText(item)
    db.save(item)
    print("=================================")
    print("Reading finished.")
