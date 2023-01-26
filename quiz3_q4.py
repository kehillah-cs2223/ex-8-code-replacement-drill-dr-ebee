def spelling_bee(word):
    spelling = f"'{word}' is spelled "
    for letter in word:
        spelling += letter.upper() + "-"
    return spelling[:-1]

print(spelling_bee("hello"))
print(spelling_bee("cat"))
print(spelling_bee("difficulty"))
