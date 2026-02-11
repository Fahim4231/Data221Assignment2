#Fahim Ahmadi
#30268421 Feb 3rd 2026

import requests
from bs4 import BeautifulSoup

def fetchSoup(pageUrl):
    #gethtmlwithuseragent
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(pageUrl, headers=headers)
    return BeautifulSoup(resp.text, "html.parser")

def getH2Headings(mainDiv):
    #collecth2headings
    blocked = ["References", "External links", "See also", "Notes"]
    headingList = []

    for tag in mainDiv.find_all("h2"):
        #wikipediakeepsheadingtextinmwheadline
        headSpan = tag.find("span", class_="mw-headline")
        if headSpan is not None:
            headingText = headSpan.get_text(strip=True)
        else:
            headingText = tag.get_text(" ", strip=True).replace("[edit]", "").strip()

        #skipblockedheadings
        skip = False
        for w in blocked:
            if w in headingText:
                skip = True
                break
        if skip:
            continue

        if headingText != "":
            headingList.append(headingText)

    return headingList

def saveHeadings(filePath, headingList):
    #saveoneperline
    out = open(filePath, "w", encoding="utf-8")
    for h in headingList:
        out.write(h + "\n")
    out.close()

def main():
    pageUrl = "https://en.wikipedia.org/wiki/Data_science"

    #parsepage
    soupObj = fetchSoup(pageUrl)

    #findmaincontentdiv
    mainContent = soupObj.find("div", id="mw-content-text")
    if mainContent is None:
        print("Main content div not found")
        return

    #extractheadings
    headingsOut = getH2Headings(mainContent)

    #writefile
    saveHeadings("headings.txt", headingsOut)

    #printtocheck
    for h in headingsOut:
        print(h)

main()
