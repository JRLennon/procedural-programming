def common_elements(a, b):
    return sorted(list(set(a).intersection(b))) # has a sorted() because of the last unit test, where it failed on [8,10,-9] == [-9,8,10]
