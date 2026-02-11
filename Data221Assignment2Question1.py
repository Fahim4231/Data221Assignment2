#Fahim Ahmadi
#30268421 Feb 3rd 2026

def cleanWord(word):
    #make lowercase
    word = word.lower()

    #punctuation to remove
    punct = ".,!?;:'\"()[]{}<>-_/\\@#$%^&*+=|~`"

    #remove punctuation from start
    while len(word) > 0 and word[0] in punct:
        word = word[1:]

    #remove punctuation from end
    while len(word) > 0 and word[-1] in punct:
        word = word[:-1]

    #count alphabetic letters
    letters = 0
    for ch in word:
        if ch.isalpha():
            letters = letters + 1

    #keep words with at least 2 letters
    if letters >= 2:
        return word

    return ""


def main():
    #open text file(go up one folder)
    f = open("../sample-file.txt", "r", encoding="utf-8")
    text = f.read()
    f.close()

    #split into tokens
    tokens = text.split()

    #clean tokens
    cleanTokens = []
    for w in tokens:
        cw = cleanWord(w)
        if cw != "":
            cleanTokens.append(cw)

    #count frequencies
    freq = {}
    for w in cleanTokens:
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1

    #sort by frequency descending
    items = list(freq.items())
    items.sort(key=lambda pair: pair[1], reverse=True)

    #print top 10 words
    top10 = items[:10]
    for word, count in top10:
        print(word, "->", count)


if __name__ == "__main__":
    main()
