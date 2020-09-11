import json
import difflib

dictionary = json.load(open('data.json'))

# to find similarity ratio between 2 words:
# difflib.SequenceMatcher(None, 'water', 'waater').ratio()

# to find a similar word with a given similarity ratio:
# difflib.get_close_matches(word, list of similar words, n, cutoff)


def get_word(akey):
    akey = akey.lower()
    if akey in dictionary:
        for aword in dictionary[akey]:
            return aword
    elif akey.title() in dictionary:
        for aword in dictionary[akey.title()]:
            return aword
    elif akey.upper() in dictionary:
        for aword in dictionary[akey.upper()]:
            return aword
    elif len(difflib.get_close_matches(akey, dictionary.keys(), cutoff=0.8)) > 0:
        thekey = difflib.get_close_matches(akey, dictionary.keys(), cutoff=0.8)[0]
        answer = input('Did you mean "%s"? If yes, print Y, otherwise print N: ' % thekey)
        if answer.upper() == 'Y':
            for aword in dictionary[thekey]:
                return aword
        elif answer.upper() == 'N':
            return 'The word does not exist. Please double check it.'
        else:
            return 'I do not understand.'
    else:
        return 'The word does not exist. Please double check it.'


print(get_word(input('Enter a word: ')))
