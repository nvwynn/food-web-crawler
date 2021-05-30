import praw
import pandas as pd

reddit = praw.Reddit(client_id='oYD4UCL93Io4sA',
                     client_secret='MocUJzdnYSGh0XTfrDhWuYzkwJCjpw',
                     user_agent='Food stamps',
                     username='SJMama',
                     password='N0h@cking!')

# This is where a subreddit is specified
subreddit = reddit.subreddit('foodstamps')

# This grabs the most up-voted topics of all-time. You can also use .hot, .new, .controversial, .top, and .gilded,
# For example, new_subreddit = subreddit.new. Note that Reddit's request limit is 1000.
top_subreddit = subreddit.top(limit=100)

for submission in subreddit.top(limit=100):
    print(submission.title, submission.id)

topics_dict = {"title": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

    topics_data = pd.DataFrame(topics_dict)

    # Create a csv file to store the structured data after processing.
    topics_data.to_csv('foodstampreddit.csv')
