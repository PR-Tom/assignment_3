def get_middle(text):
    length = len(text)
    mid = length // 2
    if length % 2 == 0:
        return text[mid - 1: mid + 1]

    return text[mid]
