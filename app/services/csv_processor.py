import pandas as pd
from app.services.category_classifier import classify_categories


def clean_transactions(file_path):

    df = pd.read_csv(file_path)

    # Remove $
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .astype(float)
        )

    # Uppercase status
    if "status" in df.columns:
        df["status"] = (
            df["status"]
            .astype(str)
            .str.upper()
        )

    # Fill missing category
    if "category" not in df.columns:
        df["category"] = ""

    # Find transactions without category
    missing_rows = []

    for _, row in df.iterrows():

        category = str(
            row.get("category", "")
        ).strip()

        if (
            category == ""
            or category.lower() == "nan"
            or category.lower() == "uncategorised"
        ):

            missing_rows.append({
                "txn_id": row.get("txn_id", ""),
                "merchant": row.get("merchant", ""),
                "description": row.get("description", "")
            })

    # Gemini Category Classification
    if missing_rows:

        classified = classify_categories(
            missing_rows
        )

        category_map = {
            item["txn_id"]: item["category"]
            for item in classified
        }

        for index, row in df.iterrows():

            txn_id = row.get("txn_id")

            if txn_id in category_map:
                df.at[index, "category"] = (
                    category_map[txn_id]
                )

    # Fill remaining null values
    df["category"] = (
        df["category"]
        .fillna("Other")
    )

    # Remove duplicates
    df = df.drop_duplicates()

    return df

