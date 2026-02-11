#Fahim Ahmadi
#30268421 Feb 3rd 2026


import csv
import requests
from bs4 import BeautifulSoup

def fetchSoup(pageLink):
    #gethtmlandmakebs4soup
    agent = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(pageLink, headers=agent, timeout=20)
    res.raise_for_status()
    return BeautifulSoup(res.text, "html.parser")

def countDataRows(htmlTable):
    #countrowsthathavecells
    rowList = htmlTable.find_all("tr")
    count = 0
    for row in rowList:
        if row.find_all(["td", "th"]):
            count += 1
    return count

def pickFirstBigTable(contentDiv, minRows):
    #findfirsttablewithenoughrows
    for tbl in contentDiv.find_all("table"):
        if countDataRows(tbl) >= minRows:
            return tbl
    return None

def buildHeaders(rowList):
    #maketheheaderlist
    if len(rowList) == 0:
        return []

    thCells = rowList[0].find_all("th")
    if thCells:
        return [c.get_text(strip=True) for c in thCells]

    maxCols = 0
    for row in rowList:
        tdCells = row.find_all("td")
        if len(tdCells) > maxCols:
            maxCols = len(tdCells)

    return [f"col{i+1}" for i in range(maxCols)]

def extractTableMatrix(rowList, headerList):
    #extractallrowsastext
    matrix = []
    colCount = len(headerList)

    for row in rowList:
        cells = row.find_all(["th", "td"])
        if not cells:
            continue

        rowVals = [c.get_text(" ", strip=True) for c in cells]

        if len(rowVals) < colCount:
            rowVals += [""] * (colCount - len(rowVals))
        elif len(rowVals) > colCount:
            rowVals = rowVals[:colCount]

        matrix.append(rowVals)

    return matrix

def writeCsv(outFile, headerList, matrix):
    #savecsvfile
    f = open(outFile, "w", newline="", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow(headerList)
    writer.writerows(matrix)
    f.close()

def main():
    pageLink = "https://en.wikipedia.org/wiki/Machine_learning"
    outFile = r"C:\Users\adfah\PycharmProjects\Data221\Data221Notes\wiki_table.csv"

    soupObj = fetchSoup(pageLink)

    contentDiv = soupObj.find("div", id="mw-content-text")
    if contentDiv is None:
        print("Content div not found")
        return

    tableObj = pickFirstBigTable(contentDiv, 3)
    if tableObj is None:
        print("No table found with at least 3 data rows")
        return

    rowList = tableObj.find_all("tr")
    headerList = buildHeaders(rowList)

    if len(headerList) == 0:
        print("Could not build headers")
        return

    matrix = extractTableMatrix(rowList, headerList)

    writeCsv(outFile, headerList, matrix)

    print("Saved table to:", outFile)
    print("Rows saved:", len(matrix))

main()

