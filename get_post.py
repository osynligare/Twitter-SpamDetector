#!/usr/bin/python

import sys
from tweety import find_post
from algorithms.kmp import kmp
from algorithms.boyer_moore import boyer_moore
from algorithms.regex import regex
import requests


def main(algorithm, userid, keyword):
    """
    main program, print posts
    :param algorithm: choice of algorithm, 1:kmp, 2:boyer moore, 3:regex
    :param username: username of twitter to parse
    :param keyword: keyword to search in post
    """
    posts = find_post(userid)
    flags = []

    if algorithm == 1:                              # kmp
        for i in range(len(posts)):
            idx = kmp(posts[i], keyword)
            if idx != -1:
                flags.append([])
                flags[len(flags) - 1].append(i)
                flags[len(flags) - 1].append(idx)
                flags[len(flags) - 1].append(idx + len(keyword))

    elif algorithm == 2:                            # boyer_moore
        for i in range(len(posts)):
            try:
                idx = int(boyer_moore(posts[i], keyword))
                if idx != -1:
                    flags.append([])
                    flags[len(flags) - 1].append(i)
                    flags[len(flags) - 1].append(idx)
                    flags[len(flags) - 1].append(idx + len(keyword))
            except:
                i = i

    elif algorithm == 3:                            # regex
        for i in range(len(posts)):
            idx = regex(posts[i], keyword)
            if idx != -1:
                flags.append([])
                flags[len(flags) - 1].append(i)
                flags[len(flags) - 1].append(idx)
                flags[len(flags) - 1].append(idx + len(keyword))

    for flag in flags:
        print(posts[flag[0]])
        posts[flag[0]] = posts[flag[0]][:flag[1]] + '<strong>' + posts[flag[0]][flag[1]:flag[2]] + '</strong>' + \
                         posts[flag[0]][flag[2]:]

    ct = 1
    for post in posts:
        post = post.encode("utf8").replace(b'\\xe2\\x80\\xa6', b'...')
        print(post)
        # print(unicodetoascii(post))


# def flag_posts(posts, flags):
#     """
#     flag posts with bold in html version
#     :param posts:
#     :param flags:
#     """
    

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    # print("Hello")
