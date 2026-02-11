#Fahim Ahmadi
#30268421 Feb 3rd 2026
#Question5:Creategradebandandgroupedsummary
import pandas as pd

def main():
    fileName = "../student.csv"  #change to "student (1).csv" if thats your filename
    df = pd.read_csv(fileName)

    #createnewcolumn:grade_band
    bands = []
    for g in df["grade"]:
        if g <= 9:
            bands.append("Low")
        elif g <= 14:
            bands.append("Medium")
        else:
            bands.append("High")

    df["grade_band"] = bands

    #groupedsummarytable
    summary = df.groupby("grade_band").agg(
        student_count=("grade", "count"),
        avg_grade=("grade", "mean"),
        avg_absences=("absences", "mean"),
        internet_rate=("internet", "mean"),
        activities_rate=("activities", "mean")
    )

    #optional:convert rates to percentages
    summary["internet_rate"] = summary["internet_rate"] * 100
    summary["activities_rate"] = summary["activities_rate"] * 100

    print(summary)

main()
