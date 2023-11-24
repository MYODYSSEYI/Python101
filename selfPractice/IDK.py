# Exercise to reverse each word  of a string
def reverse_words(Sentence):
    # Split string on whitespace
    words = Sentence.split(" ")

    # iterate list and reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]
    
    # Joining the new list of words
    res_str = " ".join(new_word_list)
    return res_str

# Given String
str1 = "My Name is Luca"
print(reverse_words(str1))