
# 📰 News Bot – AI-Powered Daily News Summarizer

This repository contains an **automated News Bot** that fetches the latest news articles from Google News RSS based on selected keywords, summarizes them using **Google Gemini 1.5 Flash**, and posts the summaries to a **Discord channel**.

It runs **daily at 9 AM Pakistan Time (4 AM UTC)** via **GitHub Actions**, ensuring you receive concise, AI-generated news updates automatically.

---

## ✨ Features

- **Smart News Retrieval**  
  Gathers articles using Google News RSS for specific, customizable keywords.

- **AI Summarization (Gemini Flash)**  
  Summarizes each article into a single sentence using Google's Gemini 1.5 Flash model.

- **Discord Integration**  
  Sends each summary directly to a specified Discord channel via webhook.

- **Automated Daily Schedule**  
  Runs automatically every day using GitHub Actions (no server or manual run required).

- **Fully Configurable**  
  Customize keywords and article limits in the Python script.

---

## ⚙️ How It Works

1. **RSS Parsing**: Uses `feedparser` to pull articles from Google News.
2. **Summarization**: Sends article title + snippet to Gemini Flash for summarizing.
3. **Posting**: Sends the result to your Discord channel via a webhook.

---

## Technologies Used

- **Python 3.10+**
- **Google Generative AI (Gemini 1.5 Flash)**
- **feedparser** (RSS handling)
- **requests** (Webhook integration)
- **GitHub Actions** (Automation and CI/CD)
- **Discord Webhooks** (For notifications)

---

## Getting Started

### 1. Fork or Clone This Repo

```bash
git clone https://github.com/mharoon1578/news-bot.git
cd news-bot
```

### 2. Set Your Secrets in GitHub

Go to your repository’s:

**Settings → Secrets and variables → Actions → New repository secret**

Add the following:

- `GEMINI_API_KEY` – Your [Google AI Studio](https://makersuite.google.com/app/apikey) API Key
- `DISCORD_WEBHOOK_URL` – Your Discord channel's webhook URL

### 3. Done! GitHub Actions Will Handle the Rest

- The bot will run **every day at 9 AM Pakistan Time**
- You can also trigger it manually from the **Actions** tab in GitHub

---

## Configuration

You can customize the bot by editing the `news_bot.py` file:

### Keywords

```python
KEYWORDS = ["artificial intelligence", "open-source AI", "growth hacking", "startups"]
```

> These are the search terms used to fetch news articles.

### Max Articles

```python
MAX_ARTICLES = 5
```

> The number of articles to summarize and post each day.

---

## Workflow (GitHub Actions)

```yaml
# .github/workflows/main.yml

name: Daily AI News via Gemini Flash

on:
  schedule:
    - cron: '0 4 * * *' # 9 AM Pakistan Time (UTC+5)
  workflow_dispatch:

jobs:
  post-news:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install google-generativeai feedparser requests

      - name: Run news bot with Gemini Flash
        env:
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python news_bot.py
```

---

## Contributing

We welcome contributions to improve this bot!  
To contribute:

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add my feature"`
4. Push to GitHub: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is open-source and licensed under the **MIT License**.  
