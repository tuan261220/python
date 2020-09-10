_end = '*'
def make_trie(*words):
    root = dict()
    for Word in words:
        current_dict = root
        for letter in Word:
            current_dict = current_dict.setdefault(letter,{})
        current_dict[_end] = _end
    return root


print(make_trie('foo','bar','baz','barz'))