"""
python scripts/social-media/youtube.py
"""
import os
import requests
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_youtube_subscribers(channel_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            subscriber_count = data['items'][0]['statistics']['subscriberCount']
            return subscriber_count
        else:
            return "Subscriber count not found"
    else:
        return f"Error: Unable to fetch channel data (Status code: {response.status_code})"

if __name__ == "__main__":
    channel_id = os.getenv('YOUTUBE_CHANNEL_ID')
    api_key = os.getenv('YOUTUBE_API_KEY')
    
    if not channel_id:
        raise ValueError("YOUTUBE_CHANNEL_ID not set in .env file")
    if not api_key:
        raise ValueError("YOUTUBE_API_KEY not set in .env file")
    
    subscribers = get_youtube_subscribers(channel_id, api_key)
    
    # Load existing social media data
    with open('./_data/social-media.yml', 'r') as file:
        data = yaml.safe_load(file)
    
    # Update subscriber count in the data structure
    data['youtube']['follower_count'] = int(subscribers)
    
    # Write updated data back to YAML file
    with open('./_data/social-media.yml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    
    print(f"YouTube subscriber count updated: {subscribers}")

