import re
import pandas as pd
import feedparser
from datetime import datetime, timezone

#Adding discovered RSS feeds into an array
#As of right now only have 1 RSS feed
RSS_FEEDS = [ "https://feeds.finance.yahoo.com/rss/2.0/headline?s=%5ENDX&region=US&lang=en-US", ]

def load_tickers(path="config/tickers.txt"):
    with open(path, "r") as f:
        return [line.strip().upper() for line in f if line.strip()]

#Testing load_tickers func    
# test = load_tickers()
# print(test)

def match_tickers(text: str, tickers):
    matches = []
    for t in tickers:
        pattern = rf"(\${t}\b|\b{t}\b)"
        if re.search(pattern, text.upper()):
            matches.append(t)
    return matches

def main():
    tickers = load_tickers()

    rows = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for e in feed.entries:
            title = getattr(e, "title", "").strip()
            summary = getattr(e, "summary", "").strip()
            published = getattr(e, "published", None)

            text_blob = f"{title} {summary}".strip()
            matched = match_tickers(text_blob, tickers)

            rows.append({
                "source_feed": url,
                "title": title,
                "summary": summary,
                "published": published,
                "matched_tickers": ",".join(matched),
                "fetched_utc": datetime.now(timezone.utc).isoformat(),
            })
    #SANITY CHECK
    #Manually added 2 tickers that were visible on the RSS feeds
    #test returns 9/20 feeds
    match_count = sum(1 for r in rows if r["matched_tickers"])
    print(f"Matched headlines: {match_count} / {len(rows)}")

    df = pd.DataFrame(rows)
    df.to_csv("data/raw_headlines.csv", index=False)
    print(f"Saved {len(df)} headlines to the data/raw_headlines.csv dir")

if __name__ == "__main__":
    main()