# myapp/tasks.py
from apscheduler.schedulers.background import BackgroundScheduler
import os
import requests
from django.conf import settings
admin_url = os.getenv('BASE_URL') + '/admin'

def ping_url():
    try:
        response = requests.get(admin_url)
        if response.status_code == 200:
            print("Successfully pinged the URL. ")
        else:
            print(f"Failed to ping the URL, status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging URL: {e}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ping_url, 'interval', seconds=30)
    scheduler.start()