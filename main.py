from task_2 import most_common_words
from task_1 import encrypt, decrypt



"""Examples:
("Abcdefghij", 1) -> "bdfhjacegi"
("Abcdefghij", 2) -> "bdfhjacegi" -> "dhaeibfjcg"
"""
# task 1 encrypt
print(encrypt("Abcdefghij", 2))
print(encrypt(None, 2))
print(encrypt('', 2))

# task 1 decrypt
print(decrypt(encrypt("Abcdefghi", 2), 2))


# task 2 - 3 most common words
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
       "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown " \
       "printer took a galley of type and scrambled it to make a type specimen book. It has survived not only " \
       "five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. " \
       "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, " \
       "and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print(most_common_words(text))
