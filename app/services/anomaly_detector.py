import pandas as pd


def detect_anomalies(df):

    anomalies = []

    for account_id, group in df.groupby("account_id"):

        median_amount = group["amount"].astype(float).median()

        for index, row in group.iterrows():

            if float(row["amount"]) > median_amount * 3:

                anomalies.append({
                    "txn_id": row["txn_id"],
                    "reason": "Amount exceeds 3x median"
                })

    return anomalies