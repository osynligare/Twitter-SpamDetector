#!/usr/bin/python

import sys
from tweety import find_post
from algorithms.kmp import kmp
from algorithms.boyer_moore import boyer_moore
from algorithms.regex import regex


def main(algorithm, userid, keyword):
    """
    get post and flag spam
    :param algorithm: choice of algorithm, 1:kmp, 2:boyer moore, 3:regex
    :param username: username of twitter to parse
    :param keyword: keyword to search in post
    """
    posts = find_post(userid)
    flags = []

    if algorithm == '1':                              # kmp
        for i in range(len(posts)):
            idx = kmp(posts[i], keyword)
            if idx != -1:
                flags.append([])
                flags[len(flags) - 1].append(i)
                flags[len(flags) - 1].append(idx)
                flags[len(flags) - 1].append(idx + len(keyword))

    elif algorithm == '2':                            # boyer_moore
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

    else:                            # regex
        for i in range(len(posts)):
            idx = regex(posts[i], keyword)
            if idx != -1:
                flags.append([])
                flags[len(flags) - 1].append(i)
                flags[len(flags) - 1].append(idx)
                flags[len(flags) - 1].append(idx + len(keyword))

    # flagging spam
    for flag in flags:
        posts[flag[0]] = posts[flag[0]][:flag[1]] + '<strong>' + posts[flag[0]][flag[1]:flag[2]] + '</strong>' + \
                         posts[flag[0]][flag[2]:]

    for post in posts:
        if 'strong' in post:
            p = '<strong>[spam]</strong> ' + post
            p = p.encode("utf8")
            print(p)
        else:
            post = post.encode("utf8")
            print(post)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
