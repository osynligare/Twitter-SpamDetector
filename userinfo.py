#!/usr/bin/python

import sys
from bs4 import BeautifulSoup as bs
import requests

def find_user(username):
    """
    find user id and profile picture url using web scraping
    :param username:
    :return: user id, profile picture url
    """
    url = 'http://gettwitterid.com/?user_name=' + username + '&submit=GET+USER+ID'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers)
    soup = bs(response.text, 'html.parser')

    # profile picture url
    profile_picture = soup.find(id='profile_photo').find('img')['src']

    # profile info
    profile_info = soup.find(class_="profile_info")

    userid = profile_info.findAll('p')[1].get_text()

    print(userid)
    print(profile_picture)

if __name__ == '__main__':
    find_user(sys.argv[1])