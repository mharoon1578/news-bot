import os
import requests
import google.generativeai as genai

# === Setup Gemini ===
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

# === Prompt Template ===
PROMPT = """
You are a tech-savvy personal news assistant. Your task is to find and summarize the **top 5 tech news articles** that match my interests.

🔍 My interests include:
- Artificial Intelligence (especially open-source models and startups)
- Growth hacking strategies
- Tech product launches or tools for indie developers
- Startup ecosystem and founder stories
- Emerging trends in deep learning, automation, and APIs

Please return a **clean list of 5 news items**, each with:
1. A **bold title**
2. A **1-sentence summary** (keep it clear and jargon-free)
3. A **source URL** (if known or assume realistic placeholder)

The tone should be professional and friendly, like you're curating news for a developer or indie founder.
"""

# === Generate News Summary ===
def get_news_from_gemini():
    response = model.generate_content(PROMPT)
    return response.text.strip()

# === Send to Discord ===
def post_to_discord(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    payload = {"content": message}
    r = requests.post(webhook_url, json=payload)
    if r.status_code != 204:
        print(f"❌ Failed to post: {r.status_code} - {r.text}")
    else:
        print("✅ Posted to Discord!")

# === Main ===
if __name__ == "__main__":
    print("🚀 Generating tech news...")
    news = get_news_from_gemini()
    print("📨 Posting to Discord...")
    post_to_discord(news)
    print("✅ Done.")
