#This chapter helps us further deepening concepts of python

def break_words(stuff):
    """This function will break sentence for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_words(words):
    #This function pops first word and then return it
    word = words.pop(0)
    return word

def print_last_word(words):
    #Print last word after popping it off.
    word = words.pop(-1)
    print(word)




