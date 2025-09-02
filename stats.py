# takes the string of the file's contents and splits it in individual words

def word_counting(bulk):
    individual_words = bulk.split()
    count = len(individual_words)
    return count

# takes the string of the file's contents, makes it all lowercase and then loops over it
# it counts individual characters including weird ones and spaces

def char_counting(lump):
    characters = {}
    lower_lump = lump.lower()
    for i in lower_lump:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

# tells sort() what to sort on (num), this function is only used inside listify
# no need to import it

def sort_on(items):
    return items["num"]

# takes the dictionary of {characters:counts} and
# adds all the alphabetical key-value pairs to a list

def listify(my_dict):
    letters_list = [{"char": k, "num": v} for k, v in my_dict.items() if k.isalpha()]
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list
