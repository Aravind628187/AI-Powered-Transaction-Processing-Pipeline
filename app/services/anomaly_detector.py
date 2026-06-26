import pandas as pd

DOMESTIC_BRANDS = [
    "Swiggy",
    "Ola",
    "IRCTC"
]


def detect_anomalies(df):

    anomalies = []

    for account_id, group in df.groupby("account_id"):

        median_amount = (
            group["amount"]
            .astype(float)
            .median()
        )

        for _, row in group.iterrows():

          

            if float(row["amount"]) > median_amount * 3:

                anomalies.append({
                    "txn_id": row["txn_id"],
                    "reason": "Amount exceeds 3x median"
                })


            if (
                str(row["currency"]).upper() == "USD"
                and str(row["merchant"]) in DOMESTIC_BRANDS
            ):

                anomalies.append({
                    "txn_id": row["txn_id"],
                    "reason": "USD transaction at domestic-only merchant"
                })

    return anomalies