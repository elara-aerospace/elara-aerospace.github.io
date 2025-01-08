"""
python scripts/social-media/linkedin.py
"""
import os
import requests
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_authorization_code():
    client_id = os.getenv('LINKEDIN_CLIENT_ID')
    redirect_uri = os.getenv('LINKEDIN_REDIRECT_URI')  # Ensure this matches what's registered
    scope = 'r_liteprofile r_emailaddress w_organization_social'  # Adjust scopes as needed
    state = 'random_string'  # Use a unique state parameter for security

    # Redirect user to LinkedIn for authorization
    authorization_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}'
    
    print(f"Please go to this URL and authorize the application:\n{authorization_url}")
    
    # Prompt user for the authorization code after they authorize the app
    auth_code = input("Enter the authorization code you received: ")
    
    return auth_code

def get_access_token(auth_code):
    client_id = os.getenv('LINKEDIN_CLIENT_ID')
    client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')
    redirect_uri = os.getenv('LINKEDIN_REDIRECT_URI')

    # Exchange authorization code for access token
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    
    response = requests.post(token_url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    
    if response.status_code != 200:
        raise Exception(f"Error fetching access token: {response.status_code} - {response.text}")
    
    return response.json()['access_token']

def get_linkedin_followers(access_token):
    organization_id = os.getenv('LINKEDIN_ORGANIZATION_ID')
    
    url = f'https://api.linkedin.com/v2/organizationalEntityFollowerStatistics?q=organizationalEntity&organizationalEntity=urn:li:organization:{organization_id}'
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-RestLi-Protocol-Version': '2.0.0'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from LinkedIn: {response.status_code} - {response.text}")
    
    data = response.json()
    
    if 'elements' in data and len(data['elements']) > 0:
        return data['elements'][0]['totalFollowerCount']
    else:
        raise Exception("No follower data found.")

if __name__ == "__main__":
    try:
        # Step 1: Get authorization code from user
        auth_code = get_authorization_code()
        
        # Step 2: Obtain access token using the authorization code
        access_token = get_access_token(auth_code)
        
        # Step 3: Get follower count from LinkedIn API
        follower_count = get_linkedin_followers(access_token)
        
        # Load existing social media data
        with open('./_data/social-media.yml', 'r') as file:
            data = yaml.safe_load(file)
        
        # Update follower count in the data structure
        data['linkedin']['follower_count'] = follower_count
        
        # Write updated data back to YAML file
        with open('./_data/social-media.yml', 'w') as file:
            yaml.dump(data, file)
        
        print(f"LinkedIn follower count updated: {follower_count}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

