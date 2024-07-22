#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    posts = data.get('data', {}).get('children', [])
    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get('data', {}).get('title'))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
