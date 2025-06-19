import os
import feedparser
import requests
import google.generativeai as genai

# --- CONFIG ---
KEYWORDS = ["artificial intelligence", "open-source AI", "growth hacking", "startups"]
MAX_ARTICLES = 5

# --- Setup Gemini Flash ---
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

# --- Fetch News from Google RSS ---
def fetch_articles():
    all_entries = []
    for keyword in KEYWORDS:
        query = keyword.replace(" ", "+")
        url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        all_entries.extend(feed.entries[:3])
    sorted_entries = sorted(all_entries, key=lambda x: x.published_parsed, reverse=True)
    return sorted_entries[:MAX_ARTICLES]

# --- Summarize Each Article ---
def summarize_article(entry):
    title = entry.title.strip()
    summary = entry.get("summary", "")
    prompt = f"Summarize the following news in one sentence:\n\nTitle: {title}\n\nSummary: {summary}"
    try:
        response = model.generate_content(prompt)
        summary_text = response.text.strip()
    except Exception as e:
        summary_text = "Summary unavailable."
        print(f"❌ Error with Gemini: {e}")
    return f"**{title}**\n{summary_text}\n<{entry.link}>"

# --- Post to Discord ---
def post_to_discord(messages):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    for msg in messages:
        res = requests.post(webhook_url, json={"content": msg})
        if res.status_code != 204:
            print(f"❌ Failed to post to Discord: {res.status_code} - {res.text}")
        else:
            print("✅ Posted to Discord")

# --- Main ---
if __name__ == "__main__":
    print("🔍 Fetching news...")
    articles = fetch_articles()

    print("🤖 Summarizing with Gemini Flash...")
    formatted_articles = [summarize_article(entry) for entry in articles]

    print("📨 Posting to Discord...")
    post_to_discord(formatted_articles)

    print("✅ Done.")
