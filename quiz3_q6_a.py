original_sentence = "Hello, how are you?"
new_sentence = ""
for letter in original_sentence:
    if letter in "aeiou":
        new_sentence += "*"
    else:
        new_sentence += letter
print(new_sentence)
