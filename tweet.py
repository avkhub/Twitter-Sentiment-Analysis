#!/usr/bin/env python
#title           :tweet.py
#description     :header for a python script.
#author          :Aditya Varma K
#usage           :python tweet.py
#python_version  :2.7
#==============================================================================
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sqlite3
import json
#import simplejson
#Variables that contains the user credentials to access Twitter API 
access_token = "XXX"
access_token_secret ="XXX"
consumer_key = "XXX"
consumer_secret = "XXX"

# access_token = "132657561-rWYbNgPmugQjuWYMmoP86NEgOBdn6O39ZUtEo04T"
# access_token_secret ="V61mtQL76GpGaey3ancZSalReNrp8augBa0m2BNsATL8I"
# consumer_key = "RsKL1JfB4ULKceU7oBPyKhEx1"
# consumer_secret = "Vz606I86qgQnQvB6I7LFHv0cSBYeDzRSBWKyuvRW7QHGsCHI1g"
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        data1 = json.loads(data)
        print data1
        f= open('data1.txt','a')
        f.write(data)
        #with open('data1.json', 'a') as outfile:
         #   json.dump(data1, outfile, indent=4)
    def on_error(self, status):
        print (status)
        # print status.ead()


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    x=raw_input('give keyword 1')
    y=raw_input('give keyword 2')
    z=raw_input('give keyword 3')
    q=raw_input('give clear to remove old data else press enter to continue')
    if q=='clear' :
        f= open('data1.txt','w')
        f.write('')
        f.close()
    else :
        pass
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[x, y, z])
