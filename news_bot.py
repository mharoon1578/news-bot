import feedparser
import requests
from transformers import pipeline
import os

# Keywords
KEYWORDS = ["artificial intelligence", "open-source AI", "growth hacking", "startups"]

# Summarizer setup
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Fetch and parse RSS feed
def fetch_articles():
    all_entries = []
    for keyword in KEYWORDS:
        url = f"https://news.google.com/rss/search?q={keyword.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        all_entries.extend(feed.entries[:3])
    return sorted(all_entries, key=lambda x: x.published_parsed, reverse=True)[:5]

# Clean HTML tags and summarize
def summarize_article(entry):
    content = entry.get("summary", "")
    summary = summarizer(content, max_length=50, min_length=15, do_sample=False)[0]['summary_text']
    return f"**{entry.title.strip()}**\n{summary.strip()}\n<{entry.link}>"

# Send to Discord
def post_to_discord(messages):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    for msg in messages:
        response = requests.post(webhook_url, json={"content": msg})
        if response.status_code != 204:
            print(f"Failed to post: {response.status_code}")

# Run bot
if __name__ == "__main__":
    print("Fetching news...")
    articles = fetch_articles()
    formatted_news = [summarize_article(entry) for entry in articles]
    print("Posting to Discord...")
    post_to_discord(formatted_news)
    print("Done.")
