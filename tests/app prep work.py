# OBJECTIVE
    # Retrieve statistics about a given Twitter user, such as that user's number of followers.
    # Optionally store these metrics in a CSV file to track changes over time.
#----------------------------------------------------------------------------------------------
# INPUTS
    # A list of existing tweets and/or hashtags and/or usernames on Twitter.com.
#----------------------------------------------------------------------------------------------
# OUTPUTS
    # A CSV file or database inventory of Twitter tweets and/or hashtags and/or usernames.
#----------------------------------------------------------------------------------------------




# Need to add an 'Environment Variable' to hide API Key from public on GitHub
# File Operations
import os
os.listdir("/Users/marinabartzokis/Desktop")

# Directory Operations
import os
os.getcwd()
os.chdir("/Users/marinabartzokis/Desktop")
os.mkdir("/Users/marinabartzokis/Desktop/freestyle/app")


# Set a new environment variable called NYU_INFO_2335
    # prereq to next step (accessing environmental variables)
echo export NYU_INFO_2335="SecretPassword123" >> ~/.bash_profile



#Accessing Environment Variables
import os
os.environ["NYU_INFO_2335"] #> SecretPassword123





#----------------------------------------------------------------------------------------------

#TWITTER_API_KEY = "IRWofH2ogy4dwf8cPxrMpiXw0"
#TWITTER_API_SECRET = "l9TwXT1pupc5QuTWLz0U7n2hfntUE4yO0x2nMO0S0X2MOSKnTS"
#TWITTER_ACCESS_TOKEN = "848698383967678464-WE45shQKyiO4CKfpiMoNoShQgq5NAMg"
#TWITTER_ACCESS_TOKEN_SECRET = "yDwj9vplgBNwE1gnj2urQ2imRhwbCt6gZxUzuHNwWU2DT"


#----------------------------------------------------------------------------------------------


pip install tweepy==3.5.0

import tweepy
from tweepy import OAuthHandler
consumer_key = "IRWofH2ogy4dwf8cPxrMpiXw0"
consumer_secret = "l9TwXT1pupc5QuTWLz0U7n2hfntUE4yO0x2nMO0S0X2MOSKnTS"
access_token = "848698383967678464-WE45shQKyiO4CKfpiMoNoShQgq5NAMg"
access_secret = "yDwj9vplgBNwE1gnj2urQ2imRhwbCt6gZxUzuHNwWU2DT"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)








import os
import tweepy

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# AUTHENTICATE

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# INITIALIZE API CLIENT

api = tweepy.API(auth)

# ISSUE REQUESTS

user = api.me() # get information about the currently authenticated user

tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user

# PARSE RESPONSES

print("---------------------------------------------------------------")
print("RECENT TWEETS BY @{0} ({1} FOLLOWERS / {2} FOLLOWING):".format(user.screen_name, user.followers_count, user.friends_count))
print("---------------------------------------------------------------")

for tweet in tweets:
    created_on = tweet.created_at.strftime("%Y-%m-%d")
    print(" + ", tweet.id_str, created_on, tweet.text)
#----------------------------------------------------------------------------------------------

import csv

user_profiles = []

user_profiles_csv = "/Users/marinabartzokis/Desktop/freestyle/data/user_profiles.csv"
headers = ["id", "followers_count", "user", "place", "lang"]
user_input_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id






otherproducts_csv = "/Users/marinabartzokis/Desktop/CRUD_App/data/otherproducts.csv"

with open(otherproducts_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for product in products:
        writer.writerow(product)



print user.screen_name


#-------------------------------------------------------
#FOLLOWER COUNT
# code from user SK13 on StackOverflow: https://stackoverflow.com/questions/20406206/how-to-get-number-of-followers-on-twitter-using-tweepy

import oauth, tweepy, sys, locale, threading
from time import localtime, strftime, sleep

def init():
    global api
    consumer_key = "..."
    consumer_secret = "..."
    access_key = "..."
    access_secret = "..."
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    user = api.get_user('...')
    print user.screen_name
    print user.followers_count
#-----------------------------
print user.followers_count
