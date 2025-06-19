import os
import feedparser
import requests
import google.generativeai as genai

# --- CONFIG ---
KEYWORDS = ["artificial intelligence", "open-source AI", "growth hacking", "startups", "New Ai Tools"]
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
    return {
        "title": title,
        "summary": summary_text,
        "link": entry.link
    }

# --- Format Digest Message ---
def format_bullet_digest(news_list):
    message = "**🔹 Today's Top Tech News:**\n\n"
    for i, item in enumerate(news_list, 1):
        message += f"{i}. **{item['title']}**\n   {item['summary']} <{item['link']}>\n\n"
    return message.strip()

# --- Post to Discord ---
def post_to_discord(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    res = requests.post(webhook_url, json={"content": message})
    if res.status_code != 204:
        print(f"❌ Failed to post to Discord: {res.status_code} - {res.text}")
    else:
        print("✅ Posted to Discord")

# --- Main ---
if __name__ == "__main__":
    print("🔍 Fetching news...")
    articles = fetch_articles()

    print("🤖 Summarizing with Gemini Flash...")
    summarized = [summarize_article(entry) for entry in articles]

    print("🧾 Formatting digest...")
    final_message = format_bullet_digest(summarized)

    print("📨 Posting to Discord...")
    post_to_discord(final_message)

    print("✅ Done.")
