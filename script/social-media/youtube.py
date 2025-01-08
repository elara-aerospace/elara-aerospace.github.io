"""
python scripts/social-media/youtube.py
"""
import os
from googleapiclient.discovery import build
import yaml

def get_youtube_followers():
    api_key = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    channel_id = os.getenv('YOUTUBE_CHANNEL_ID')
    request = youtube.channels().list(part='statistics', id=channel_id)
    response = request.execute()

    subscriber_count = response['items'][0]['statistics']['subscriberCount']

    return int(subscriber_count)

if __name__ == "__main__":
    follower_count = get_youtube_followers()
    
    with open('./_data/social-media.yml', 'r') as file:
        data = yaml.safe_load(file)
    
    data['youtube']['follower_count'] = follower_count
    
    with open('./_data/social-media.yml', 'w') as file:
        yaml.dump(data, file)

