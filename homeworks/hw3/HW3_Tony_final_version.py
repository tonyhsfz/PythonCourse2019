import imp
import sys
import tweepy
import csv

# load the twitter key
twitter = imp.load_source('twit', '/Users/Saint ZiC/lpthw/secret/start_twitter.py')
api = twitter.client

# Questions 1-4: Getting Information about WUSTL's friends and followers.
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


# Questions 5-6: Getting the Information of WUSTLPoliSci's friends and followers.
#   and WUSTLPoliSci's friends' friends and followers' followers.
# repeat the process in the previous few sections to scrape the followers of WUSTLPoliSci
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
