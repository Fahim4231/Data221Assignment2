#Fahim Ahmadi
#30268421 Feb 3rd 2026

import csv
import requests
from bs4 import BeautifulSoup

def loadSoup(webAddress):
    #downloadpageandparsehtml
    uaHeader = {"User-Agent": "Mozilla/5.0"}
    pageReply = requests.get(webAddress, headers=uaHeader, timeout=20)
    pageReply.raise_for_status()
    return BeautifulSoup(pageReply.text, "html.parser")

def rowsWithCells(tblObj):
    #countrowswithtdorth
    allTr = tblObj.find_all("tr")
    cellRows = 0
    for trTag in allTr:
        if trTag.find_all(["td", "th"]):
            cellRows += 1
    return cellRows

def chooseTable(mainArea, needRows):
    #grabfirsttablewithenoughrows
    for tableTag in mainArea.find_all("table"):
        if rowsWithCells(tableTag) >= needRows:
            return tableTag
    return None

def makeHeaderList(trList):
    #createheadersfromfirstroworcolnames
    if len(trList) == 0:
        return []

    thList = trList[0].find_all("th")
    if thList:
        names = []
        for th in thList:
            names.append(th.get_text(strip=True))
        return names

    biggest = 0
    for tr in trList:
        tdList = tr.find_all("td")
        if len(tdList) > biggest:
            biggest = len(tdList)

    names = []
    for i in range(biggest):
        names.append("col" + str(i+1))
    return names

def tableToGrid(trList, colNames):
    #extracttabletextgrid
    grid = []
    width = len(colNames)

    for trTag in trList:
        cellTags = trTag.find_all(["th", "td"])
        if not cellTags:
            continue

        values = []
        for c in cellTags:
            values.append(c.get_text(" ", strip=True))

        if len(values) < width:
            values += [""] * (width - len(values))
        elif len(values) > width:
            values = values[:width]

        grid.append(values)

    return grid

def dumpCsv(savePath, colNames, grid):
    #writecsvoutput
    outHandle = open(savePath, "w", newline="", encoding="utf-8")
    outWriter = csv.writer(outHandle)
    outWriter.writerow(colNames)
    outWriter.writerows(grid)
    outHandle.close()

def main():
    webAddress = "https://en.wikipedia.org/wiki/Machine_learning"
    savePath = r"C:\Users\adfah\PycharmProjects\Data221\Data221Notes\wiki_table.csv"

    soupDoc = loadSoup(webAddress)

    mainArea = soupDoc.find("div", id="mw-content-text")
    if mainArea is None:
        print("Content div not found")
        return

    foundTable = chooseTable(mainArea, 3)
    if foundTable is None:
        print("No table found with at least 3 data rows")
        return

    trList = foundTable.find_all("tr")
    colNames = makeHeaderList(trList)

    if len(colNames) == 0:
        print("Could not build headers")
        return

    grid = tableToGrid(trList, colNames)

    dumpCsv(savePath, colNames, grid)

    print("Saved table to:", savePath)
    print("Rows saved:", len(grid))

main()
