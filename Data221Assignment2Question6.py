#Fahim Ahmadi
#30268421 Feb 3rd 2026
import pandas as pd

def main():
    #changethisifthefilenameisdifferent
    fileName = "../crime.csv"  #or "crime (1).csv"

    #load data
    df = pd.read_csv(fileName)

    #create risk column
    riskList = []
    for v in df["ViolentCrimesPerPop"]:
        if v >= 0.50:
            riskList.append("HighCrime")
        else:
            riskList.append("LowCrime")
    df["risk"] = riskList

    #group and compute average unemployment
    avgUnemp = df.groupby("risk")["PctUnemployed"].mean()

    #print in a clear format
    high = avgUnemp.get("HighCrime", float("nan"))
    low = avgUnemp.get("LowCrime", float("nan"))

    print("Average PctUnemployed by risk group")
    print("HighCrime ->", high)
    print("LowCrime  ->", low)

main()
