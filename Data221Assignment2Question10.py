#Fahim Ahmadi
#30268421 Feb 3rd 2026

def findLinesContaining(filePath, keyWord):
    #returnlistof(linenumber,linetext)thatcontainkeywordcaseinsensitive
    found = []

    f = open(filePath, "r", encoding="utf-8")
    lineNum = 1
    for line in f:
        if keyWord.lower() in line.lower():
            found.append((lineNum, line.strip()))
        lineNum = lineNum + 1
    f.close()

    return found


def main():
    #testfunctiononsamplefile
    filePath = "sample-file.txt"
    keyWord = "lorem"

    matches = findLinesContaining(filePath, keyWord)

    #printmatchcount
    print("Number of matching lines:", len(matches))

    #printfirst3matches
    print("First 3 matching lines:")
    for lineNum, text in matches[:3]:
        print(lineNum, text)


main()
