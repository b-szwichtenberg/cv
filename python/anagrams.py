def frequency(characters):
    frequency = {}
    for char in characters:
        frequency[char] = frequency.get(char,0) + 1
    return frequency

word_1 = "taktak"
word_2 = "katkat"

if (frequency(word_1) == frequency(word_2)):
    print(word_1 + " and " + word_2 + " are anagrams.")
else:
    print(word_1 + " and " + word_2 + "are not anagrams. ")

"""
word_1 = "taktak"
word_2 = "katkat"

word_1 = word_1.lower()
word_2 = word_2.lower()

if(len(word_1) == len(word_2)):
    sorted_word1 = sorted(word_1)
    sorted_word2 = sorted(word_2)

    if(sorted_word1 == sorted_word2):
        print(word_1 + " and " + word_2 + " are anagrams.")
    else:
        print(word_1 + " and " + word_2 + "are not anagrams. ")

else:
    print(word_1 + " and " + word_2 + " are not anagrams.")
"""