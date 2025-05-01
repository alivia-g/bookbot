def count_words(content):
    words = content.split()
    #print(f"{len(words)} words found in the document")
    return len(words)

def count_chars(content):
    lowercase = content.lower()
    counts = {}
    for c in lowercase:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def print_report(counts):  # {'char': count}
    sorted_list = []
    for count in counts:
        sorted_list.append({"char": count, "num": counts[count]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list