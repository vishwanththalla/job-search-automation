# TODO: Implement job search
import pandas as pd

company_file = "data/company_jobs.csv"
market_file = "data/market_jobs.csv"
output_file = "data/jobs.csv"

company_df = pd.read_csv(company_file)

try:
    market_df = pd.read_csv(market_file)
except:
    market_df = pd.DataFrame()

df = pd.concat(
    [company_df, market_df],
    ignore_index=True
)

df.drop_duplicates(
    subset=["company", "title", "apply_link"],
    inplace=True
)

df.to_csv(output_file, index=False)

print(f"Merged {len(df)} jobs")