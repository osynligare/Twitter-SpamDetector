#!/usr/bin/python

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

def find_post(userid):
    """
    find posts of username
    :param username:
    :return: posts of username
    """
    results = api.GetUserTimeline(user_id=userid)

    posts = []

    for result in results:
        json_str = json.dumps(result._json)
        data = json.loads(json_str)
        posts.append(data.get('text'))

    return posts
