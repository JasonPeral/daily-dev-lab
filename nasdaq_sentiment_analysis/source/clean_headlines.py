import pandas as pd 

def main():
    df = pd.read_csv("data/raw_headlines.csv")

    #normalize / clean the raw headlines data
    df["title"] = df["title"].fillna("").str.strip()
    df["summary"] = df["summary"].fillna("").str.strip()
    df["matched_tickers"] = df["matched_tickers"].fillna("").str.strip()

    # Filtering to ticker related headlines only
    before = len(df)
    df = df[df["matched_tickers"].str.len() > 0].copy()
    after_filter = len(df)

    # De-dupe data
    df = df.drop_duplicates(subset=["title"])

    after_dedupe = len(df)
    df.to_csv("data/clean_headlines.csv", index=False)

    print(f"Raw headlines:      {before}")
    print(f"After ticker match: {after_filter}")
    print(f"After de-dupe:      {after_dedupe}")
    print("Saved: data/clean_headlines.csv")

if __name__ == "__main__":
    main()