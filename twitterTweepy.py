#!/usr/bin/python3

import tweepy as tp
import time
import os

# twitter credentials for api access

consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_secret = ' '

# twitter api login code

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# posts your statement
post = 'this is a test post using tweepy'

api.update_status(post)
