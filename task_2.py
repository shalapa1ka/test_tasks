# import collections
import re


def most_common_words(text: str) -> list:
    text = text.lower()
    pattern = re.compile(r"[a-z']+")
    data = re.findall(pattern, text)

    # result = [item[0] for item in collections.Counter(data).most_common()]
    count_dict = {}
    for item in data:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 0

    result = list(count_dict)
    return result[:3] if len(result) >= 3 else []
