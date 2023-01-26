def search(text, keyword):
    if keyword in text:
        index = text.find(keyword)
        after_keyword = index + 40
        excerpt = text[index: after_keyword]
        return excerpt
    else:
        return "Keyword not found."

full_text = """
Men at some time are masters of their fates:
The fault, dear Brutus, is not in our stars,
But in ourselves, that we are underlings.
Brutus and Caesar: what should be in that 'Caesar'?
Why should that name be sounded more than yours?
"""

print(search(full_text, "Caesar"))
