import re


def most_common_words(text: str) -> list:
    text = text.lower()
    pattern = re.compile(r"[a-z']+")
    data = re.findall(pattern, text)

    count_dict = {}
    for item in data:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    sorted_tuples = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    result = list(sorted_dict)

    return result[:3] if len(result) >= 3 else []
