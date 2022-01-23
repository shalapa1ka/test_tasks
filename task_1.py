def encrypt(text: str, n: int) -> str:
    if not text or n <= 0:
        return text
    text = text.lower()
    return encrypt(text[1::2] + text[::2], n - 1)


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    even = encrypted_text[:len(encrypted_text) // 2]
    odd = encrypted_text[len(encrypted_text) // 2:]
    result = ''
    if not (len(odd) == len(even)):
        even += ' '
    for item in zip(odd, even):
        result += "".join(item)
    return decrypt(result.strip(), n - 1)
