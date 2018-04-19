from tweety import find_post, find_user
from StringMatch import kmp


def main(algorithm, username, keyword):
    """
    main program, print posts
    :param algorithm: choice of algorithm, 1:kmp, 2:boyer moore, 3:regex
    :param username: username of twitter to parse
    :param keyword: keyword to search in post
    """
    imageUrl = "<img src=" + find_user(username)[1] + "></img>"
    posts = find_post(username)
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
            idx = kmp(posts[i], keyword)
            if idx != -1:
                flags.append([])
                flags[len(flags) - 1].append(i)
                flags[len(flags) - 1].append(idx)
                flags[len(flags) - 1].append(idx + len(keyword))

    elif algorithm == 3:                            # regex
        for i in range(len(posts)):
            idx = kmp(posts[i], keyword)
            if idx != -1:
                flags.append([])
                flags[len(flags) - 1].append(i)
                flags[len(flags) - 1].append(idx)

    flag_posts(posts, flags)
    print(posts)


def flag_posts(posts, flags):
    """
    flag posts with bold in html version
    :param posts:
    :param flags:
    """
    for flag in flags:
        posts[flag[0]] = posts[flag[0]][:flag[1]-1] + '<strong>' + posts[flag[1]-1:flag[2]-1] + '</strong>' + posts[:flag[2]-1]


main(1,'ridwankamil','a')