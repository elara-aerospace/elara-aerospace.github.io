"""
python scripts/social-media/twitter.py
"""
import os
import tweepy
import yaml

def get_twitter_followers():
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET_KEY'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    
    api = tweepy.API(auth)
    
    user = api.get_user(screen_name=os.getenv('TWITTER_USERNAME'))
    return user.followers_count

if __name__ == "__main__":
    follower_count = get_twitter_followers()
    
    with open('./_data/social-media.yml', 'r') as file:
        data = yaml.safe_load(file)
    
    data['twitter']['follower_count'] = follower_count
    
    with open('./_data/social-media.yml', 'w') as file:
        yaml.dump(data, file)

