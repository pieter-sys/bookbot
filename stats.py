# takes the string of the file's contents and splits it in individual words

def word_counting(bulk):
    individual_words = bulk.split()
    count = len(individual_words)
    return count

def char_counting(lump):
    characters = {}
    lower_lump = lump.lower()
    for i in lower_lump:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters
