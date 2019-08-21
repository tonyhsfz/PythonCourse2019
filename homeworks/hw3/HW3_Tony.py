import imp
import sys
import tweepy
import csv

# load the twitter key
twitter = imp.load_source('twit', '/Users/Saint ZiC/lpthw/secret/start_twitter.py')
api = twitter.client

# Create a csv file storing the result
with open('HW3_WUfollowers.csv', 'w') as f:
	# create five headers
	w = csv.DictWriter(f, fieldnames = ("id", "name", "num followers", "num tweets", "type"))
	w.writeheader()
	# for each item in WUSTL's followers
	for item in tweepy.Cursor(api.followers_ids, 'WUSTL').items():
		# create a dictionary for writing csv row
		follower = {}
		# record its id
		follower["id"] = item
		try:
			# try getting the details by its id
			follower_info = api.get_user(item)
		except:
			print("ERROR: Unable to get the info of id number: " + str(item))
		else:
			# record its screen name
			follower["name"] = follower_info.screen_name
			# record its number of followers
			follower["num followers"] = follower_info.followers_count
			# record its number of tweets
			follower["num tweets"] = follower_info.statuses_count
			# categorize the account into celebrity, layman, or expert
			if follower_info.followers_count > 1000:
				follower["type"] = "celebrity"
			elif follower_info.followers_count < 100:
				follower["type"] = "layman"
			else:
				follower["type"] = "expert"
				# write the csv row
				w.writerow(follower)

# repeat the previous procedure for WUSTL's friends
with open('HW3_WUfriends.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("id", "name", "num followers", "num tweets", "type"))
	w.writeheader()
	for item in tweepy.Cursor(api.friends, 'WUSTL').items():
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

# open the csv file recording the WUSTL's followers
with open('HW3_WUfollowers.csv', 'r') as f:
	reader = csv.DictReader(f)
	# create lists for comparison
	num_followers = []
	num_tweets = []
	name = []
	# for each row (account) in the csv file
	for i in reader:
		# read its number of followers and append to the list
		num_followers.append(int(i["num followers"]))
		# read its number of tweets and append to the list
		num_tweets.append(int(i["num tweets"]))
		# read its screen name and append to the list
		name.append(i["name"])
	# find the maximum number of followers
	Max_followers = max(num_followers)
	# find the maximum number of tweets
	Max_tweets = max(num_tweets)
	# find the account with maximum number of followers
	Max_followers_name = name[num_followers.index(Max_followers)]
	# find the account with maximum number of tweets
	Max_tweets_name = name[num_tweets.index(Max_tweets)]

# print out the results
print("\nAmong the followers of @WUSTL, \"@" + str(Max_tweets_name) + "\" has the greatest number of total tweets.")
print("\t\"@" + str(Max_tweets_name) + "\" has " + str(Max_tweets) + " tweets in total.")
print("\nAmong the followers of @WUSTL, \"@" + str(Max_followers_name) + "\" has the greatest number of followers.")
print("\t\"@" + str(Max_followers_name) + "\" has " + str(Max_followers) + " followers in total.")

# repeat the previous section to find the answers of the remaining questions
with open('HW3_WUfriends.csv', 'r') as f:
	reader = csv.DictReader(f)
	num_followers = []
	name = []
	num_tweets_layman = []
	layman = []
	num_tweets_expert = []
	expert = []
	num_tweets_celebrity = []
	celebrity = []
	for i in reader:
		num_followers.append(int(i["num followers"]))
		name.append(i["name"])
		if i["type"] == "layman":
			num_tweets_layman.append(int(i["num tweets"]))
			layman.append(i["name"])
		elif i["type"] == "expert":
			num_tweets_expert.append(int(i["num tweets"]))
			expert.append(i["name"])
		elif i["type"] == "celebrity":
			num_tweets_celebrity.append(int(i["num tweets"]))
			celebrity.append(i["name"])
	Max_followers = max(num_followers)
	Max_tweets_layman = max(num_tweets_layman)
	Max_tweets_expert = max(num_tweets_expert)
	Max_tweets_celebrity = max(num_tweets_celebrity)
	Max_followers_name = name[num_followers.index(Max_followers)]
	Max_tweets_layman_name = layman[num_tweets_layman.index(Max_tweets_layman)]
	Max_tweets_expert_name = expert[num_tweets_expert.index(Max_tweets_expert)]
	Max_tweets_celebrity_name = celebrity[num_tweets_celebrity.index(Max_tweets_celebrity)]

print("\nAmong those who @WUSTL follows, \"@" + str(Max_followers_name) + "\" has the greatest number of followers.")
print("\t\"@" + str(Max_followers_name) + "\" has " + str(Max_followers) + " followers in total.")
print("\nAmong those who @WUSTL follows, \"@" + str(Max_tweets_layman_name) + "\" has the greatest number of total tweets within the layman group.")
print("\t\"@" + str(Max_tweets_layman_name) + "\" has " + str(Max_tweets_layman) + " tweets in total.")
print("\nAmong those who @WUSTL follows, \"@" + str(Max_tweets_expert_name) + "\" has the greatest number of total tweets within the expert group.")
print("\t\"@" + str(Max_tweets_expert_name) + "\" has " + str(Max_tweets_expert) + " tweets in total.")
print("\nAmong those who @WUSTL follows, \"@" + str(Max_tweets_celebrity_name) + "\" has the greatest number of total tweets within the celebrity group.")
print("\t\"@" + str(Max_tweets_celebrity_name) + "\" has " + str(Max_tweets_celebrity) + " tweets in total.")
