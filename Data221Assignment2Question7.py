#Fahim Ahmadi
#30268421 Feb 3rd 2026
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"

    #add user-agent so wikipedia does not block request
    headers = {"User-Agent": "Mozilla/5.0"}

    #download the page
    response = requests.get(url, headers=headers)
    html = response.text

    #parse html
    soup = BeautifulSoup(html, "html.parser")

    #1)print title from <title>
    titleTag = soup.find("title")
    if titleTag is not None:
        print("Title:", titleTag.get_text().strip())
    else:
        print("Title: Not found")

    #2)find main content div
    contentDiv = soup.find("div", id="mw-content-text")
    if contentDiv is None:
        print("Main content div not found")
        return

    #3)find the first paragraph with at least 50 characters
    paragraphs = contentDiv.find_all("p")

    firstGoodPara = None
    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) >= 50:
            firstGoodPara = text
            break

    if firstGoodPara is None:
        print("No paragraph with at least 50 characters was found")
    else:
        print("\nFirst paragraph (50+ chars):")
        print(firstGoodPara)

main()
