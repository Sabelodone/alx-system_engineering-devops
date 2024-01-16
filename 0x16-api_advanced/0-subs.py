import requests

def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad requests
        if response.status_code == 302:
            print(f"Subreddit '{subreddit}' is a redirect. Returning 0 subscribers.")
            return 0

        data = response.json()
        return data.get('data', {}).get('subscribers', 0)

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found. Returning 0 subscribers.")
        else:
            print(f"Error: {err}")

        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(f"{subscribers_count}")
