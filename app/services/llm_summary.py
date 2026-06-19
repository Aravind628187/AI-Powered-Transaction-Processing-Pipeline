import google.generativeai as genai
import json

genai.configure(
    api_key="AQ.Ab8RN6Lt70BT00poFSxc2vfMKrEnxK_YVJkB_IE4O6pD6hCF8w"
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

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception:

        return f"""
        Total INR Spend: {total_inr}
        Total USD Spend: {total_usd}

        Top Merchants:
        {", ".join(top_merchants)}

        Anomalies Found:
        {anomaly_count}
        """