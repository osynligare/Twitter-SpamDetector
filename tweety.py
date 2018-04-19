#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import requests
import twitter
import json

# load our API credentials
config = {}
exec(open("config.py").read(), config)

# Create an Api instance.
api = twitter.Api(consumer_key=config["consumer_key"],
                  consumer_secret=config["consumer_secret"],
                  access_token_key=config["access_key"],
                  access_token_secret=config["access_secret"])


def find_user(username):
    """
    find user id and profile picture url using web scraping
    :param username:
    :return: user id, profile picture url
    """
    url = 'http://gettwitterid.com/?user_name='+username+'&submit=GET+USER+ID'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers)
    soup = bs(response.text, 'html.parser')

    # profile picture url
    profile_picture = soup.find(id='profile_photo').find('img')['src']

    # profile info
    profile_info = soup.find(class_="profile_info")

    userid = profile_info.findAll('p')[1].get_text()
    
    return userid, profile_picture


def find_post(username):
    """
    find posts of username
    :param username:
    :return: posts of username
    """
    userid = find_user(username)[0]
    results = api.GetUserTimeline(user_id=userid)

    posts = []

    for result in results:
        json_str = json.dumps(result._json)
        data = json.loads(json_str)
        posts.append (data.get('text'))

    return posts
