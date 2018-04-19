import re


def regex(text, pattern):
    """
    string matching using regex algorithm
    :param text:
    :param pattern:
    :return: index of first occurrence of pattern in text
    """
    text = text.lower()
    pattern = pattern.lower()

    res = re.finditer(pattern, text)

    idx = [r.span() for r in res]

    if len(idx) != 0:
        return idx[0][0]
    else:
        return -1


regex("asdfasdf", "asdk")