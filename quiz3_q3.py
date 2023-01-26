sentence = "Hello, how are you?"
for word in sentence.split(" "):
    first_letter = word[0].upper()
    rest_of_word = word[1:].lower()
    print(first_letter + rest_of_word)
