#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Define the base URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set the headers to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Define the parameters for pagination
    params = {'limit': 100}
    if after:
        params['after'] = after

    # Make the API request
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Extract the list of hot posts
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    # Check if there is a next page
    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


# Example usage:
if __name__ == "__main__":
    result = recurse('programming')
    if result is not None:
        print(len(result))
    else:
        print("None")
