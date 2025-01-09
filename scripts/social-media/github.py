"""
python scripts/social-media/github.py
"""
import os
import requests
import yaml
from dotenv import load_dotenv

def get_github_followers():
    load_dotenv()  # Load environment variables from .env file
    
    username = os.getenv('GH_USERNAME')
    token = os.getenv('GH_TOKEN')
    
    url = f'https://api.github.com/users/{username}'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        if 'followers' in data:
            return data['followers']
        else:
            print(f"Error: 'followers' key not found in GitHub API response. Response: {data}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching GitHub followers: {e}")
        return None

if __name__ == "__main__":
    follower_count = get_github_followers()
    
    if follower_count is not None:
        try:
            with open('./_data/social-media.yml', 'r') as file:
                data = yaml.safe_load(file)
            
            if 'github' not in data:
                data['github'] = {}
            
            data['github']['follower_count'] = follower_count
            
            with open('./_data/social-media.yml', 'w') as file:
                yaml.dump(data, file)
            
            print(f"GitHub follower count updated: {follower_count}")
        except Exception as e:
            print(f"Error updating YAML file: {e}")
    else:
        print("Failed to update GitHub follower count")

