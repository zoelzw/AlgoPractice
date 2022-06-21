def lengthOfLastWord(s):
    words = []
    string = " ".join(s.split())
    for word in string.split(" "):
        words.append(word)
    # words.remove('')
    return len(words[-1])

print(lengthOfLastWord("hello world  moon   "))