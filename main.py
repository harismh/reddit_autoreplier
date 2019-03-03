import praw
import re
import os
import sys
import configparser

config = configparser.ConfigParser()
config.read('praw.ini')
search_phrase = config["CONFIG"]["search_phrase"]
delete_phrase = config["CONFIG"]["delete_phrase"]
reply_phrase = config["CONFIG"]["reply_phrase"]
max_length = int(config["CONFIG"]["max_length"])
reddit = praw.Reddit("USER")
subreddit = reddit.subreddit(config["CONFIG"]["subreddit"])

if not os.path.isfile("posts_replied_to.txt"):
  posts_replied_to = []
else:
  with open("posts_replied_to.txt", 'r') as file:
    posts_replied_to = file.read()
    posts_replied_to = posts_replied_to.split('\n')
    posts_replied_to = list(filter(None, posts_replied_to))

try: 
	print("Bot started. Fetching comments...")
	for comment in subreddit.stream.comments():
		if len(comment.body) <= max_length and re.search(search_phrase, comment.body, re.IGNORECASE):
			if comment.id not in posts_replied_to:
				print("Bot replying to comment: {0}".format(comment.id))
				try:
	 				comment.reply(reply_phrase)
	 				posts_replied_to.append(comment.id)
				except:
					print("Error replying to comment")
		if len(comment.body) <= max_length and re.search(delete_phrase, comment.body, re.IGNORECASE) and comment.parent().body != "[deleted]":
			print("Bot deleting comment: {0}".format(comment.parent().id))
			try:
				comment.parent().delete()	
			except:
				print("Error deleting comment.")
except KeyboardInterrupt:
	with open("posts_replied_to.txt", "w") as file:
		for id in posts_replied_to:
			file.write(id + "\n")
	print("\n--------")
	print("Replies saved to posts_replied_to.txt")

sys.exit();