# takes the string of the file's contents and splits it in individual words
def word_counting(bulk):
    individual_words = bulk.split()
    count = len(individual_words)
    return count
