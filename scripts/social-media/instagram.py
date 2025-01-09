"""
python scripts/social-media/instagram.py
"""
import os
import requests
import yaml

def get_instagram_followers():
    access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    user_id = os.getenv('INSTAGRAM_USER_ID')
    
    url = f'https://graph.instagram.com/v12.0/{user_id}?fields=followers_count&access_token={access_token}'
    
    response = requests.get(url)
    data = response.json()
    
    return data['followers_count']

if __name__ == "__main__":
    follower_count = get_instagram_followers()
    
    with open('./_data/social-media.yml', 'r') as file:
        data = yaml.safe_load(file)
    
    data['instagram']['follower_count'] = follower_count
    
    with open('./_data/social-media.yml', 'w') as file:
        yaml.dump(data, file)

