import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def generate_summary(
    total_inr,
    total_usd,
    top_merchants,
    anomaly_count
):

    prompt = f"""
    Generate a JSON summary for the following transaction data.

    Total INR Spend: {total_inr}
    Total USD Spend: {total_usd}

    Top Merchants:
    {", ".join(top_merchants)}

    Anomaly Count:
    {anomaly_count}

    Return JSON with:
    - total_spend_inr
    - total_spend_usd
    - top_merchants
    - anomaly_count
    - narrative
    - risk_level
    """

    for attempt in range(3):

        try:

            response = model.generate_content(prompt)

            return response.text

        except Exception as e:

            print(
                f"Attempt {attempt + 1} failed: {e}"
            )

            time.sleep(2 ** attempt)

    return {
        "total_spend_inr": total_inr,
        "total_spend_usd": total_usd,
        "top_merchants": top_merchants,
        "anomaly_count": anomaly_count,
        "narrative": "LLM summary unavailable.",
        "risk_level": "unknown",
        "llm_failed": True
    }