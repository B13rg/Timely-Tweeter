#-=- Coding: Python UTF-8 -=-

import tweepy, time, sys 

argfile = str(sys.argv[1])

print ("Timely Tweeter")
print (" ")
print ("Posting so you don't have to")

#Twitter Account info
    #Place Keys and Tokens bewteen the quotes
CONSUMER_KEY = '' #The Consumer Key (API Key)
CONSUMER_SECRET = '' #The Consumer Secret (API Secret)
ACCESS_KEY = '' #The Access Token
ACCESS_SECRET = '' #The Access Token Secret
SLEEPY_TIME = #Time to wait in seconds between tweets

#Now it checks in with Twitter and gets authenticated
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r') #Opens file
f=filename.readlines() #Pulls data from file
filename.close() #Closes file
print ("Pulled data from file")

for line in f:
    api.update_status(line)
    time.sleep(SLEEPY_TIME) #Time to wait
