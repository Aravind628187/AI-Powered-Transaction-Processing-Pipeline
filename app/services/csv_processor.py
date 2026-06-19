import pandas as pd


def clean_transactions(file_path):

    df = pd.read_csv(file_path)

    # remove $
    df["amount"] = (
        df["amount"]
        .astype(str)
        .str.replace("$", "", regex=False)
    )

    # uppercase status
    df["status"] = (
        df["status"]
        .astype(str)
        .str.upper()
    )

    # fill category
    df["category"] = (
        df["category"]
        .fillna("Uncategorised")
    )

    # remove duplicates
    df = df.drop_duplicates()

    return df