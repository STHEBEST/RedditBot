import praw
import requests
import json
import time 

reddit = praw.Reddit(
    client_id="<Your client ID>",
    client_secret="<Your secret key>",
    user_agent="<Your user agent>",
    username="<Your username>",
    password="<Your password>"
)

res = requests.get("https://zenquotes.io/api/random")
new_res =  res.json()

quote = new_res[0]['q']
author = new_res[0]['a']

subreddit = reddit.subreddit("television")
sad_quotes = []


for submission in subreddit.hot(limit=10):

    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("----------")
                print(comment.body)
                comment.reply(f"{quote} - {author}")
                time.sleep(660)