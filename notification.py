import requests 
import sys

NOTIFICATION_URLS = "Your notification end point url"


# function to get posts to show notification

def getNotifications():

    try:
        response = requests.get(NOTIFICATION_URLS)
        response.raise_for_status() 
        return response.json().get('posts', []) 
    except requests.exceptions.RequestException as e:
        print(f"Unable to load notifications from {NOTIFICATION_URLS}: {e}")
        sys.exit(1) 

