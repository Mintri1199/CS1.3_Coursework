# Problem: Write a function that takes 2 array of words (strings), and returns a new array of words in the first array
# that are not in the second array.


def redact_words(words, banned_words):  # O(n + m) -> O(n)

    # Check if the text array is empty
    if len(words) == 0:
        return []

    # Turn the array of banned words into a set
    banned_words_set = set(banned_words)  # O(m) where m is the number of words in the banned word array

    filtered_words = []

    for word in words:  # O(n) where n is the number of words in the text array
        if banned_words_set.__contains__(word.lower()) is False:  # O(1)
            filtered_words.append(word)  # O(1)

    return filtered_words  # O(1)


text_array = 'A a a jump over the dog.'.split()
banned_word = ['dog']
filter_array = redact_words(text_array, banned_word)
print(filter_array)