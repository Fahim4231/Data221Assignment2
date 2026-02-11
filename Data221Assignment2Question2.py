#Fahim Ahmadi
#30268421 Feb 3rd 2026
#Question2:Top5bigramfrequencies

def cleanWord(word):
    #lowercase
    word = word.lower()

    #punctuation to remove from start/end
    punct = ".,!?;:'\"()[]{}<>-_/\\@#$%^&*+=|~`"

    #strip punctuation from beginning
    while len(word) > 0 and word[0] in punct:
        word = word[1:]

    #strip punctuation from end
    while len(word) > 0 and word[-1] in punct:
        word = word[:-1]

    #count alphabetic letters
    letters = 0
    for ch in word:
        if ch.isalpha():
            letters = letters + 1

    #must have at least 2 letters
    if letters >= 2 and word != "":
        return word
    return ""


def main():
    #read file
    fileName = "../sample-file.txt"
    f = open(fileName, "r", encoding="utf-8")
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

    #count bigrams
    bigramFreq = {}
    for i in range(len(cleanTokens) - 1):
        bg = cleanTokens[i] + " " + cleanTokens[i + 1]

        if bg in bigramFreq:
            bigramFreq[bg] = bigramFreq[bg] + 1
        else:
            bigramFreq[bg] = 1

    #sort by count descending
    items = list(bigramFreq.items())
    items.sort(key=lambda pair: pair[1], reverse=True)

    #print top5
    top5 = items[:5]
    for bigram, count in top5:
        print(bigram, "->", count)


main()
