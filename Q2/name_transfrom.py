import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s','--style')
parser.add_argument('-v','--variable')
args = parser.parse_args()

AVAILABLE_STYLES = {"kebab-case", "snake_case", "PascalCase", "camelCase"}

def partition_var(var: str):
    words = []
    start = 0
    end = 0
    for l in var:
        if l == "-" or l == "_":    #snake_case and kabab-case
            words.append(var[start:end])
            start = end+1
        elif l.isupper() and end > 0:   #Pascal Case and camelCase
            words.append(var[start:end].lower())
            start = end
        end = end + 1
    if end > start:
        words.append(var[start:end].lower())
    return words

def capitalize(arr: [], capitalize_first: bool):
    capitalized = []
    for i in range(len(arr)):
        if (i == 0 and not capitalize_first):
            word = arr[i]
        else:
            word = arr[i].capitalize()
        capitalized.append(word)
    return "".join(capitalized)

def stylize_var(original_var: str, style: str):
    arr = partition_var(original_var)
    if style == "kebab-case":
        return "-".join(arr)
    elif style == "snake_case":
        return "_".join(arr)
    elif style == "PascalCase":
        return capitalize(arr, True)
    elif style == "camelCase":
        return capitalize(arr, False)

if args.style not in AVAILABLE_STYLES:
    print("Please pick one style to transform from ", AVAILABLE_STYLES)
else:
    with open("transformed_variable_name.txt", "w") as f:
        f.write(stylize_var(args.variable, args.style))
        f.close()
