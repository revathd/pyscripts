# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 16:10:50 2016

@author: revathi.nalla
"""


import tweepy
import csv

 
# Consumer keys and access tokens, used for OAuth

consumer_key="xxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret="xxxxxxxxxxxxxxxxxxxx"
access_token="xxx-xxxxx"
access_token_secret="xxxxxxxxxxxxxxxx"
 
# OAuth process, using the keys and tokens

 
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.entities["user_mentions"]] for tweet in alltweets]
	
	transform = outtweets
	tt1={}
	for test in transform:
         if test[3]:
			tt1= test[3]
			print tt1
			#t=[d['user_mentions'] for d in tt1]
			#[d['user_mentions'] for d in tt1 if 'user_mentions' in d]
			print tt1[0].get("screen_name")
    
 
	#test2 = [test[0],test[1],test[2]  for test in transform]
     
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("India")
