def part(pattern):
    """
    find suffix and prefix match table for pattern
    :param pattern:
    :return: table
    """
    table = [0]

    for i in range(1, len(pattern)):
        j = table[i-1]
        while j > 0 and pattern[j] != pattern[i]:
            j = table[j-1]
        table.append(j+1 if pattern[j] == pattern[i] else j)
    
    return table


def kmp(text, pattern):
    """
    kmp pattern matching algorithm
    :param text:
    :param pattern:
    :return: index of first occurrence of pattern in text
    """
    if len(pattern) > len(text):
        return -1
    else:
        pattern = pattern.lower()
        text = text.lower()
        table = part(pattern)
        j = 0

        for i in range(len(text)):
            if text[i] == pattern[j]:
                if j == len(pattern)-1:
                    return i - len(pattern) + 1
                else:
                    j = j+1
            else:   # text[i] != pattern[j]
                j = table[j-1]
                i = i + len(pattern) - j
        
        return -1
