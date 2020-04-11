import requests
from bs4 import BeautifulSoup
def get_upcoming_events(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    events = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')

    for event in events:
        event_details = dict()