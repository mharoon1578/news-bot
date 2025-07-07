# News Bot

## 📰 Introduction

This repository houses an automated **News Bot** designed to keep you updated with the latest news on specific topics.  
Leveraging **Google News RSS feeds** for fetching articles and **Google Gemini 1.5 Flash** for concise summarization,  
this bot efficiently delivers key insights directly to your **Discord channel**.  
It runs automatically **daily using GitHub Actions**, ensuring you never miss important updates.

---

## 🚀 Features

- **Targeted News Fetching**: Retrieves news articles from Google News RSS feeds based on predefined keywords.  
- **AI-Powered Summaries**: Uses Google Gemini 1.5 Flash to generate a one-sentence summary for each article.  
- **Discord Integration**: Posts the summarized articles directly to a specified Discord channel via a webhook.  
- **Automated Scheduling**: Runs daily at **9 AM Pakistan Time (4 AM UTC)** via GitHub Actions.  
- **Customizable Content**: Easily adjust keywords and the number of articles to fetch.

---

## 🛠️ Technologies Used

- **Python** – Bot logic  
- **Google Generative AI (Gemini 1.5 Flash)** – For advanced summarization  
- **feedparser** – Parses RSS/Atom feeds  
- **requests** – HTTP requests to Discord Webhook  
- **GitHub Actions** – For automation  
- **Discord** – Target platform for news updates

---

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.10+
- Google Gemini API Key (from [Google AI Studio](https://aistudio.google.com/))
- Discord Webhook URL (Settings → Integrations → Webhooks → New Webhook)

### Installation Steps

```bash
git clone https://github.com/mharoon1578/news-bot.git
cd news-bot
````

#### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, use:

```
google-generativeai
feedparser
requests
```

---

## Configure Environment Variables

### Local `.env` File

Create a `.env` file in the root folder:

```env
GEMINI_API_KEY=your_google_gemini_api_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

Install dotenv support (optional but recommended):

```bash
pip install python-dotenv
```

And load it in `news_bot.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

### GitHub Secrets

* Go to your repo → **Settings → Secrets and Variables → Actions**
* Add:

  * `GEMINI_API_KEY`
  * `DISCORD_WEBHOOK_URL`

---

## Usage

### Run Locally

```bash
python news_bot.py
```

This fetches news, summarizes it, and posts to Discord using your `.env` file.

### Run Automatically via GitHub Actions

The workflow runs **daily at 9 AM Pakistan Time (UTC+5)**.
To run it manually:

1. Go to **Actions** tab
2. Click **"Daily AI News via Gemini Flash"**
3. Hit **"Run workflow"**

---

## Configuration

You can modify the following variables in `news_bot.py`:

```python
KEYWORDS = ["artificial intelligence", "open-source AI", "growth hacking", "startups"]
MAX_ARTICLES = 5
```

* `KEYWORDS`: List of topics you want to fetch news for
* `MAX_ARTICLES`: Max number of articles per run

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes
4. Commit:

   ```bash
   git commit -m 'Add feature: your-feature'
   ```
5. Push:

   ```bash
   git push origin feature/your-feature
   ```
6. Open a **Pull Request**

---

## 📄 License

This project is open-source under the **MIT License**.
