def capitals(word):
    # create an empty list to store the indices of capital letters
    capital_indices = []

    # iterate over the characters in the word and check if they are uppercase
    for i in range(len(word)):
        if word[i].isupper():
            capital_indices.append(i)

    return capital_indices