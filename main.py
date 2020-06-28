import praw
import re
import os
import sys

REDDIT = praw.reddit("USER")
SUBREDDIT = REDDIT.subreddit("testingground4bots")
MAX_LENGTH = 20
SEARCH_PHRASE = "!dropthemic"
DELETE_PHRASE = "delete pls"
REPLY_PHRASE = '''#🎤 Drop.

***

^(I'm a bot. Reply with **delete pls** to remove.)
'''

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", 'r') as file:
        posts_replied_to = file.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))

try:
    print("Bot started. Fetching comments...")
    for comment in SUBREDDIT.stream.comments():
        if len(comment.body) <= MAX_LENGTH and re.search(SEARCH_PHRASE, comment.body, re.IGNORECASE):
            if comment.id not in posts_replied_to:
                print("Bot replying to comment: {0}".format(comment.id))
                try:
                    comment.reply(REPLY_PHRASE)
                    posts_replied_to.append(comment.id)
                    reply_count += 1
                except:
                    print("Error replying to comment")
        if len(comment.body) <= MAX_LENGTH and re.search(DELETE_PHRASE, comment.body, re.IGNORECASE) and comment.parent().body != "[deleted]":
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

sys.exit()
