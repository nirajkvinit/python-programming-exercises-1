# Note: binary_search isn't optimal but works

import statistics

def isthere(alist, anumber):
    if anumber in alist:
        return True
    else:
        return False


def binary_search(alist, anumber):
    median = int(statistics.median(alist))

    if len(alist) > 2:
        if anumber == alist[median]:
            return True
        elif anumber > alist[median]:
            newlist = list(alist[median:])
            return binary_search(newlist, anumber)
        elif anumber < alist[median]:
            newlist = list(alist[:median])
            return binary_search(newlist, anumber)
    else:
        if alist[0] == anumber or alist[1] == anumber:
            return True
        else:
            return False

