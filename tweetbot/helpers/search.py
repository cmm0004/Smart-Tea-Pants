# import oauth2
# from tweetbot.helpers.APIKeys import APIKeys
# import time
# import urllib.request as urllib2
# import json
import datetime
import tweepy


class Search(object):

    def __init__(self, TWEETBOT):
        self.TWEETBOT = TWEETBOT

   
    #     self.apikeys = APIKeys()
        
    #     self.apikeys = APIKeys()
    #     self.url1 ="https://api.twitter.com/1.1/search/tweets.json"
    #     self.params = {"oauth_version":"1.0",
    #               "oauth_nonce": oauth2.generate_nonce(),
    #               "oauth_timestamp":int(time.time())
    #               }

    #     self.consumer = oauth2.Consumer(key=self.apikeys.consumer_key,
    #                                secret=self.apikeys.consumer_secret)
    #     self.token = oauth2.Token(key=self.apikeys.access_token,
    #                          secret=self.apikeys.access_token_secret)

    #     self.params["oauth_consumer_key"] = self.consumer.key
    #     self.params["oauth_token"] = self.token.key
        
    # def search(self, query, count):
        
    #     for i in range(1):
    #         url = self.url1
    #         self.params["q"] = query
    #         self.params["count"] = count
    #         req = oauth2.Request(method="GET", url=url, parameters=self.params)
    #         signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    #         req.sign_request(signature_method, self.consumer, self.token)
    #         headers = req.to_header()
    #         url = req.to_url()
    #         try:
    #             response = urllib2.Request(url)

    #             data = json.load(urllib2.urlopen(response))
    #             if data:
    #                 return data
    #             else:
    #                 return False
    #         except urllib2.HTTPError:
    #             print("Http error" + str(urllib2.HTTPError.code))
    #             return False

    # def favorite_hashtag(self, hashtag_query):
    #     query = self.search(hashtag_query, 5)
    #     if query:
    #         statuses = query['statuses']
    #         for tweet in statuses:
    #             try:
    #                 TWITTER_BOT.create_favorite(tweet['id'])
    #                 print("SUCCESS status: " + str(tweet['id']))
    #                 print(datetime.datetime.now())
    #             except tweepy.TweepError:
    #                 print("favorite failed on status: " + str(tweet['id']))
    #                 print(datetime.datetime.now())

    #     else:
    #         return     

    def get_statuses(self, query, count):
        return [status for status in tweepy.Cursor(self.TWEETBOT.search, q=query).items(count)]
        
        
