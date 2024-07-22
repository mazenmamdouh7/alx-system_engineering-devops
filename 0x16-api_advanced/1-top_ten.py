#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    # Define the base URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set the headers to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Define the parameters for limiting the number of posts
    params = {'limit': 10}

    # Make the API request
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON response
    data = response.json()

    # Extract the list of hot posts
    posts = data.get('data', {}).get('children', [])
    if not posts:
        print(None)
        return

    # Print the titles of the first 10 hot posts
    for post in posts:
        print(post.get('data', {}).get('title'))

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
