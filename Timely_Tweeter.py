#-=- Coding: Python UTF-8 -=-

import tweepy, time, sys, random

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

#Now it checks in with Twitter and gets authenticated
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r') #Opens file
f=filename.readlines() #Pulls data from file
filename.close() #Closes file
print ("Pulled data from file")

minimum = raw_input("Set minimum time (min):")
maximum = raw_input("Set maximum time (min):")

for line in f:
    SLEEPY_TIME = random.randint(minimum, maximum)
    api.update_status(line)
    print ("---Tweet sent---")
    print ("Sleeping for ", SLEEPY_TIME/60, " hours.")
    time.sleep(SLEEPY_TIME) #Time to wait
