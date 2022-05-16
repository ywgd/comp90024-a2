import tweepy as tw
import json
import couchdb

api_key= '8k7SzAflvtcFmaqJsTiqzylYa'
api_key_secret= 'qPqhLwP77RiuWRgLn8KKPscFLX6PQprPXtrYiaJLxH0Hpe2846'
access_token= '1517355964617297920-mOWbcyxo7Zr9SXsRN8nXIn9zrm2NpT'
access_token_secret= 'zvJ7znhMV4ZmVG6fKl3t4w7e4McNUU7x8cCTGNympdwqD'


couch = couchdb.Server('http://admin:admin@172.26.130.142:5984/')
db = couch['streaming_data']


class listener(tw.Stream):

    def on_data(self, data):

        print(data)

        json_data = json.loads(data)
        #id = json_data['id']

        db.save(json_data)

        # with open('twitterdata_extended_done_comma.json', 'a', encoding='utf-8') as tf:
        #     json_data = json.loads(data)
        #
        #     is_not_retweeted = False
        #     is_not_quoted = False
        #     has_place = False
        #     has_text = True
        #
        #     # if there is no text: throw it away
        #     if "text" not in json_data:
        #         has_text = False
        #
        #     if has_text:
        #         if ("retweeted_status" not in json_data) and ('RT @' not in json_data['text']):
        #             # this is for not retweeted only
        #             is_not_retweeted = True
        #
        #         if "quoted_status" not in json_data:
        #             # this is for not quoted only
        #             is_not_quoted = True
        #
        #         if ("place" in json_data) and json_data['place'] != None:
        #             # check if the value of place is None or not
        #             has_place = True
        #
        #         if is_not_retweeted and is_not_quoted and has_place:
        #             if "extended_tweet" in json_data:
        #                 temp_text = json_data['extended_tweet']['full_text']
        #                 json_data['text'] = temp_text
        #                 print("This tweet is with extended text.")
        #             else:
        #                 print("This tweet do not have extended text.")
        #
        #
        #             # #print(json_data)
        #             # tf.write('\n')
        #             # json.dump(json_data, tf)
        #             # tf.write(',')
        #             db
        #
        #             print("========================= succeed in writing file =========================")

    def on_error(self, status):
        if status == 420:
            #returning False in on_data disconnects the stream
            return False
        print(status)


if __name__ == '__main__':

    auth = tw.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    stream = listener(
        api_key, api_key_secret, access_token, access_token_secret
    )

    try:
        #stream.filter(languages=['en'], track = ['covid, coronavirus'])
        stream.filter(languages=['en'], track=['covid', 'coronavirus', 'covid-19', 'COVID'], locations=[144.312,-38.506,145.894,-37.160])

        print("Start streaming.")

    except KeyboardInterrupt:
        print("Keyboard Stopped.")

    finally:
        print('Streaming Finished.')
        stream.disconnect()

