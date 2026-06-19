import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

CATEGORIES = [
    "Food",
    "Shopping",
    "Travel",
    "Transport",
    "Utilities",
    "Cash Withdrawal",
    "Entertainment",
    "Other"
]


def classify_categories(transactions):
    """
    transactions:
    [
        {
            "txn_id": "TXN1001",
            "merchant": "Swiggy",
            "description": "Food Order"
        }
    ]
    """

    if not transactions:
        return []

    prompt = f"""
You are a transaction categorization system.

Assign exactly one category for each transaction.

Allowed Categories:
{", ".join(CATEGORIES)}

Transactions:
{json.dumps(transactions, indent=2)}

Return ONLY valid JSON.

Example:

[
  {{
    "txn_id": "TXN1001",
    "category": "Food"
  }},
  {{
    "txn_id": "TXN1002",
    "category": "Travel"
  }}
]
"""

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)

    except Exception as e:

        print("Category Classification Error:", e)

        return [
            {
                "txn_id": tx["txn_id"],
                "category": "Other"
            }
            for tx in transactions
        ]