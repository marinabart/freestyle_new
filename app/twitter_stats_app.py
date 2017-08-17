import pip
import tweepy


from tweepy import OAuthHandler
TWITTER_API_CONSUMER_KEY = "IRWofH2ogy4dwf8cPxrMpiXw0"
TWITTER_API_CONSUMER_SECRET = "l9TwXT1pupc5QuTWLz0U7n2hfntUE4yO0x2nMO0S0X2MOSKnTS"
TWITTER_API_ACCESS_TOKEN = "848698383967678464-WE45shQKyiO4CKfpiMoNoShQgq5NAMg"
TWITTER_API_ACCESS_SECRET = "yDwj9vplgBNwE1gnj2urQ2imRhwbCt6gZxUzuHNwWU2DT"


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(TWITTER_API_CONSUMER_KEY, TWITTER_API_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_API_ACCESS_TOKEN, TWITTER_API_ACCESS_SECRET)

    api = tweepy.API(auth)

    user_handle = input("Enter Twitter handle: @")


    print("---------------------------------------------------------------")
    print ("Statistics for @" + (user_handle) + ":")

    data = api.get_user(user_handle)
    print("---------------------------------------------------------------")
    print ("Followers: " + str(data.followers_count))
    print ("Tweets: " + str(data.statuses_count))
    print ("Favorites: " + str(data.favourites_count))
    print ("Friends: " + str(data.friends_count))
    print ("Appears on " + str(data.listed_count) + " lists")

#----------------------------------------------------------------


# PARSE RESPONSES

user = api.me() # get information about the currently authenticated user

tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user


print("---------------------------------------------------------------")

#----------------------------------------------------------------


# WRITE TWITTER ACCOUNTS TO FILE

import csv

twitter_handle_stats_csv = "/Users/marinabartzokis/Desktop/freestyle/data/twitter_handle_stats.csv"


with open(twitter_handle_stats_csv, "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["handle", "followers", "tweets", "favorites", "friends", "appears on"])
    #writer.writeheader() # uses fieldnames set above
    writer.writerow({"handle": (user_handle), "followers": str(data.followers_count), "tweets": str(data.statuses_count), "favorites": str(data.favourites_count), "friends": str(data.friends_count), "appears on": str(data.listed_count)})
