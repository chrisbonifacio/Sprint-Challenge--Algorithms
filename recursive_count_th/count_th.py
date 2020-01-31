'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


from datetime import datetime


def count_th(word):
    # if "th" is not found in word
    index = len(word) - 1

    def recursive_count(index):
        if index < 0:
            return 0

        if index < 0:
            index = 0

        print("ITERATION: ", index)
        print("LETTER 1 and LETTER 2: ", word[index], word[index - 1])

        if word[index] + word[index - 1] == "ht":
            return 1 + recursive_count(index - 1)

        return 0 + recursive_count(index - 1)

    return recursive_count(index)


start = datetime.now()
print(count_th("thereforeththth"))
print(datetime.now() - start)
