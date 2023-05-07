def reverse_words(str):
    newStr = []
    for i in str.split(" "):
        newStr.append(i[::-1])
    return " ".join(newStr)

print(reverse_words("kokot pica u holica spinava rit"))
