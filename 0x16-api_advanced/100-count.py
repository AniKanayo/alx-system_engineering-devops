#!/usr/bin/python3
""" A recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    # To initialize count_dict if it is not passed as an argument
    if count_dict is None:
        count_dict = {}

    # Defining the URL and headers for the API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Define the parameters for the API request
    params = {"limit": 100}
    if after is not None:
        params["after"] = after

    # Send the API request and handle errors
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return

    # Extract the data from the response
    data = response.json().get("data")
    if data is None:
        return

    # Process the titles of the hot articles
    for child in data.get("children"):
        title = child.get("data").get("title").lower()
        for word in word_list:
            if " {} ".format(word.lower()) in " {} ".format(title):
                if word.lower() in count_dict:
                    count_dict[word.lower()] += 1
                else:
                    count_dict[word.lower()] = 1

    # Recursively call the function if there are more articles
    after = data.get("after")
    if after is not None:
        count_words(subreddit, word_list, count_dict, after)

    # Print the results in descending order of counts, and then alphabetically
    sorted_words = sorted(count_dict.keys(), key=lambda w: (-count_dict[w], w))
    for word in sorted_words:
        print("{}: {}".format(word, count_dict[word]))
