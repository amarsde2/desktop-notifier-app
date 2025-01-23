"""
Author: Er. Amar kumar
Professional: Senior Software Enginner

"""

"""
Library used in this project

1. Time Module
2. Plyer Library

"""


import time 
from plyer import notification
from notification import getNotifications

  
posts = getNotifications()
    
for post in posts:
    notification.notify(
        title=post['title'],
        message=post['body'],
        app_name="Desktop Notifier App",
        timeout=10
    )
    time.sleep(15)
