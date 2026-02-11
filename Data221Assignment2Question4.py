#Fahim Ahmadi
#30268421 Feb 3rd 2026
#Question4:Filterstudentdataandsavecsv

import pandas as pd

def main():
    #changethisifthefilenameisdifferent
    fileName = "../student.csv"

    #loadcsvintoDataFrame
    df = pd.read_csv(fileName)

    #filter:studytime>=3,internet==1,absences<=5
    filtered = df[(df["studytime"] >= 3) & (df["internet"] == 1) & (df["absences"] <= 5)]

    #savefiltereddata
    filtered.to_csv("high_engagement.csv", index=False)

    #printnumberofstudentsandaveragegrade
    count = len(filtered)

    #avoidcrashifzerorows
    if count == 0:
        avgGrade = 0
    else:
        avgGrade = filtered["grade"].mean()

    print("Students saved:", count)
    print("Average grade:", avgGrade)

main()
