import requests
import time

# 🔧 CONFIG
BASE_URL = "http://127.0.0.1:8000/honeypot"  # Change to your deployed link
API_KEY = "your_api_key_here"

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

# 🎯 SCENARIOS
SCENARIOS = [
    {
        "scenarioId": "bank_fraud",
        "initialMessage": "URGENT: Your SBI account has been compromised. Share your account number and OTP immediately.",
        "turns": [
            "Please confirm your account number 1234567890123456",
            "Share OTP 458921 to verify",
            "Call me at +91-9876543210 for support",
            "Also confirm UPI scammer.fraud@fakebank"
        ]
    },
    {
        "scenarioId": "upi_fraud",
        "initialMessage": "Congratulations! You have won Rs. 5000 cashback from Paytm. Verify your UPI.",
        "turns": [
            "Send your UPI ID",
            "Use cashback.scam@fakeupi to receive money",
            "Contact support at +91-8765432109",
            "Confirm immediately"
        ]
    },
    {
        "scenarioId": "phishing_link",
        "initialMessage": "You won iPhone 15 Pro for Rs. 999! Click here: http://amaz0n-deals.fake-site.com/claim?id=12345",
        "turns": [
            "Offer valid only 10 minutes",
            "Login using your bank account",
            "Email us at offers@fake-amazon-deals.com",
            "Confirm payment quickly"
        ]
    }
]


def run_scenario(scenario):
    print(f"\n🚀 Testing Scenario: {scenario['scenarioId']}")
    session_id = scenario["scenarioId"] + "_test"

    messages = [scenario["initialMessage"]] + scenario["turns"]

    for i, msg in enumerate(messages):
        payload = {
            "sessionId": session_id,
            "message": {
                "text": msg
            }
        }

        try:
            response = requests.post(BASE_URL, json=payload, headers=HEADERS)
            data = response.json()

            print(f"\nTurn {i+1}")
            print("Scammer:", msg)
            print("Honeypot Reply:", data.get("reply"))

            time.sleep(0.5)

        except Exception as e:
            print("❌ Error:", e)
            break


if __name__ == "__main__":
    for scenario in SCENARIOS:
        run_scenario(scenario)

    print("\n✅ Testing Completed")
