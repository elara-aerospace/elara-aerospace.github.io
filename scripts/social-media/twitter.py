"""
python scripts/social-media/twitter.py
"""
import os
import requests
import yaml
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

def get_twitter_followers():
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    username = os.getenv('TWITTER_USERNAME')
    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "v2FollowerCountPython"
    }

    # First, get the user ID
    user_url = f"https://api.twitter.com/2/users/by/username/{username}"
    response = requests.get(user_url, headers=headers)
    
    if response.status_code != 200:
        if response.status_code == 429:
            print("Rate limit exceeded. Skipping update.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return None

    user_id = response.json()['data']['id']

    # Now, get the follower count
    follower_url = f"https://api.twitter.com/2/users/{user_id}?user.fields=public_metrics"
    response = requests.get(follower_url, headers=headers)
    
    if response.status_code != 200:
        if response.status_code == 429:
            print("Rate limit exceeded. Skipping update.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return None

    follower_count = response.json()['data']['public_metrics']['followers_count']
    return follower_count

def update_yaml_file(follower_count):
    yaml_path = './_data/social-media.yml'
    
    # Read the existing YAML file
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Update the follower count
    data['twitter']['follower_count'] = follower_count
    
    # Write the updated data back to the YAML file
    with open(yaml_path, 'w') as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    follower_count = get_twitter_followers()
    
    if follower_count is not None:
        update_yaml_file(follower_count)
        print(f"Updated follower count to {follower_count}")
    else:
        print("Follower count not updated.")

