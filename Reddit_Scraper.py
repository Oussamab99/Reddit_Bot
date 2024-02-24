import praw

import tkinter as tk
from tkinter import scrolledtext

# You need to create a Reddit app to get API access
# Replace YOUR_CLIENT_ID, YOUR_CLIENT_SECRET, and YOUR_USER_AGENT with your own credentials

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Specify the subreddit to scrape
subreddit = reddit.subreddit("programmerhumor")

# Create the GUI window
root = tk.Tk()
root.title("Reddit Scraper")

# Create a text box to display the results
text_box = scrolledtext.ScrolledText(root, width=50, height=10)
text_box.pack() 

def scrape_subreddit():
    text_box.delete("1.0", tk.END) # Clear the text box
    for submission in subreddit.hot(limit=10): # Limit the number of submissions to 10
        post_info = f"Title: {submission.title}\nScore: {submission.score}\nNumber of comments: {submission.num_comments}\n\n"
        text_box.insert(tk.END, post_info)

#button to scrape   
button = tk.Button(root, text="Scrape", command=scrape_subreddit)
button.pack()

# Start the GUI event loop
root.mainloop()