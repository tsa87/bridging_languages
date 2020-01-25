def partition_var(var: str):
    words = []

    start = 0
    end = 0
    for l in var:
        # snake_case and kabab-case
        if l == "-" or l == "_":
            words.append(var[start:end])
            start = end+1
        # Pascal Case and camelCase
        elif l.isupper() and end > 0:
            words.append(var[start:end].lower())
            start = end
        end = end + 1

    if end > start:
        words.append(var[start:end].lower())

    return words

def stylize_var(arr: [], style: str):
    arr = partition_var(arr)

    if style == "kebab":
        return "-".join(arr)
    elif style == "snake":
        return "_".join(arr)
    elif style == "pascal":
        return capitalize(arr, True)
    elif style == "camel":
        return capitalize(arr, False)

def capitalize(arr: [], capitalize_first: bool):
    capitalized = []
    for i in range(len(arr)):
        if (i == 0 and not capitalize_first):
            word = arr[i]
        else:
            word = arr[i].capitalize()
        capitalized.append(word)
    return "".join(capitalized)
