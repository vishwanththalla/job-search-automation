import pandas as pd

OUTPUT_FILE = "data/market_jobs.csv"

jobs = [
    {
        "company": "Example Company",
        "title": "DevOps Engineer",
        "location": "Remote",
        "apply_link": "https://example.com",
        "source": "market"
    }
]

df = pd.DataFrame(jobs)

df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved {len(df)} market jobs")