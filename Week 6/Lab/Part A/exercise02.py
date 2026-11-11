def alphabetical_sort(string):
    return ''.join(sorted(sorted(string), key=lambda x: (x.casefold(), x.swapcase()))) # returned char sorted in alphabetical order, lowercase before uppercase as shown in expected outputs

