#Fahim Ahmadi
#30268421 Feb 3rd 2026
#Question3:NearDuplicateLines(NoImports)

def normalizeLine(line):
    #lowercase
    line = line.lower()

    #remove whitespace and punctuation by keeping only letters/digits
    norm = ""
    for ch in line:
        if ch.isalnum():
            norm = norm + ch
    return norm


def main():
    fileName = "../sample-file.txt"

    #read all lines
    f = open(fileName, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()

    #group lines by normalized version
    groups = {}
    order = []  #keeps the order of first time we see each normalized key

    lineNum = 1
    for line in lines:
        original = line.rstrip("\n")
        key = normalizeLine(original)

        #skip empty normalized lines (optional safety)
        if key == "":
            lineNum = lineNum + 1
            continue

        if key not in groups:
            groups[key] = []
            order.append(key)

        groups[key].append((lineNum, original))
        lineNum = lineNum + 1

    #collect near-duplicate sets (size >= 2) in file order
    dupKeys = []
    for key in order:
        if len(groups[key]) >= 2:
            dupKeys.append(key)

    #print number of near-duplicate sets
    print(len(dupKeys))

    #print first two sets (if they exist)
    setsToShow = 2
    if len(dupKeys) < 2:
        setsToShow = len(dupKeys)

    for i in range(setsToShow):
        key = dupKeys[i]
        print("\nSet", i + 1)
        for lineNum, original in groups[key]:
            print(str(lineNum) + ":", original)


main()
