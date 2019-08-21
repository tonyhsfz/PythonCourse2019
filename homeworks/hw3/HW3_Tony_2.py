import imp
import sys
import tweepy
import csv

# load the twitter key
twitter = imp.load_source('twit', '/Users/Saint ZiC/lpthw/secret/start_twitter.py')
api = twitter.client

# repeat the process in the previous script to scrape the followers of WUSTLPoliSci
with open('HW3_WUPSfollowers.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("id", "name", "num followers", "num tweets", "type"))
  w.writeheader()
  for item in tweepy.Cursor(api.followers_ids, 'WUSTLPoliSci').items():
	  follower = {}
	  follower["id"] = item
	  try:
		  follower_info = api.get_user(item)
	  except:
		  print("ERROR: Unable to get the info of id number: " + str(item))
	  else:
		  follower["name"] = follower_info.screen_name
		  follower["num followers"] = follower_info.followers_count
		  follower["num tweets"] = follower_info.statuses_count
		  if follower_info.followers_count > 1000:
			  follower["type"] = "celebrity"
		  elif follower_info.followers_count < 100:
			  follower["type"] = "layman"
		  else:
			  follower["type"] = "expert"
		  w.writerow(follower)

# repeat the process in the previous script to scrape the friends of WUSTLPoliSci
with open('HW3_WUPSfriends.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("id", "name", "num followers", "num tweets", "type"))
	w.writeheader()
	for item in tweepy.Cursor(api.friends, 'WUSTLPoliSci').items():
		friend = {}
		friend["id"] = item.id
		try:
			friend_info = api.get_user(item.id)
		except:
			print("ERROR: Unable to get the info of id number: " + str(item.id))
		else:
			friend["name"] = friend_info.screen_name
			friend["num followers"] = friend_info.followers_count
			friend["num tweets"] = friend_info.statuses_count
			if friend_info.followers_count > 1000:
				friend["type"] = "celebrity"
			elif friend_info.followers_count < 100:
				friend["type"] = "layman"
			else:
				friend["type"] = "expert"
			w.writerow(friend)

# read the csv file recording WUSTLPoliSci's followers
with open('HW3_WUPSfollowers.csv', 'r') as f:
	reader = csv.DictReader(f)
	name = []
    # create a list of names recording all the names of non-celebrity followers of WUSTLPoliSci
	for i in reader:
		if i["type"] != "celebrity":
			name.append(i["name"])

# repeat the process to scrape the followers of the followers of WUSTLPoliSci (in the list)
with open('HW3_WUPSfollowers_followers.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("id", "name", "num tweets"))
	w.writeheader()
	for i in name:
        # create a list, tweepy, to record the followers of the followers
        # the purpose of doing this is to prevent Error by using "try...except..."
		tweepy = []
		try:
			user = api.get_user(i)
			tweepy = user.followers_ids()
		except:
			print("ERROR: Unable to get the followers of: " + str(i))
		else:
			for item in tweepy:
				follower = {}
				follower["id"] = item
				try:
					follower_info = api.get_user(item)
				except:
					pass
				else:
					follower["name"] = follower_info.screen_name
					follower["num tweets"] = follower_info.statuses_count
					w.writerow(follower)

# repeat the process above the find the friends of friends of WUSTLPoliSci
with open('HW3_WUPSfriends.csv', 'r') as f:
	reader = csv.DictReader(f)
	name = []
	for i in reader:
		if i["type"] != "celebrity":
			name.append(i["name"])

with open('HW3_WUPSfriends_friends.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("id", "name", "num tweets"))
	w.writeheader()
	for i in name:
		tweepy = []
		try:
			tweepy = tweepy.Cursor(api.friends, i).items()
		except:
			print("ERROR: Unable to get the friends of: " + str(i))
		else:
			for item in tweepy:
				friend = {}
				friend["id"] = item.id
				try:
					friend_info = api.get_user(item.id)
				except:
					pass
				else:
					friend["name"] = friend_info.screen_name
					friend["num tweets"] = friend_info.statuses_count
					w.writerow(friend)

# create lists for finding the account with maximum tweets
num_tweets = []
name = []
# read the WUSTLPoliSci followers info and record them in the list
with open('HW3_WUPSfollowers.csv', 'r') as f:
	reader = csv.DictReader(f)
	for i in reader:
		num_tweets.append(int(i["num tweets"]))
		name.append(i["name"])
# read the WUSTLPoliSci followers' followers info and append them in the list
with open('HW3_WUPSfollowers_followers.csv', 'r') as f:
	reader = csv.DictReader(f)
	for i in reader:
		num_tweets.append(int(i["num tweets"]))
		name.append(i["name"])
# find the maximum
Max_tweets = max(num_tweets)
Max_tweets_name = name[num_tweets.index(Max_tweets)]
# print out the results
print("\nAmong the followers of @WUSTL and their followers, \n\t\"@" + str(Max_tweets_name) + "\" has the greatest number of total tweets.")
print("\t\"@" + str(Max_tweets_name) + "\" has " + str(Max_tweets) + " tweets in total.")

# repeat the previous section for WUSTLPoliSci's friends' friends
num_tweets = []
name = []
with open('HW3_WUPSfriends.csv', 'r') as f:
	reader = csv.DictReader(f)
	for i in reader:
		num_tweets.append(int(i["num tweets"]))
		name.append(i["name"])

with open('HW3_WUPSfriends_friends.csv', 'r') as f:
	reader = csv.DictReader(f)
	for i in reader:
		num_tweets.append(int(i["num tweets"]))
		name.append(i["name"])

Max_tweets = max(num_tweets)
Max_tweets_name = name[num_tweets.index(Max_tweets)]

print("\nAmong those who @WUSTL follows and those who they follow, \n\t\"@" + str(Max_tweets_name) + "\" has the greatest number of total tweets.")
print("\t\"@" + str(Max_tweets_name) + "\" has " + str(Max_tweets) + " tweets in total.")
