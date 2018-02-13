# -*- coding: utf-8 -*-

import time
from TwitterAPI import TwitterAPI

from auth_xxxx import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

tweet_number = 0
stringToTrack = "#trump" #change to what you want

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
print 'Twitter ready!'

s = api.request('statuses/filter', {'track':stringToTrack})

for item in s:
        if "text" in item:
            tweet_number = tweet_number + 1
            print("Tweet number: " + str(tweet_number))
            print item['user']['screen_name'].encode('utf-8') + ' tweeted: ' + item['text'].encode('utf-8')
            print("--------")
            print("")
