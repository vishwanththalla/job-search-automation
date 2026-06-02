# TODO: Generate Excel
import pandas as pd
from datetime import datetime
from pathlib import Path

INPUT_FILE = "data/scored_jobs.csv"

df = pd.read_csv(INPUT_FILE)

df = df.sort_values(
    by="match_score",
    ascending=False
)

Path("output/archive").mkdir(
    parents=True,
    exist_ok=True
)

today = datetime.now().strftime("%Y_%m_%d")

daily_file = "output/daily_jobs.xlsx"
archive_file = f"output/archive/jobs_{today}.xlsx"

df.to_excel(
    daily_file,
    index=False
)

df.to_excel(
    archive_file,
    index=False
)

print("Excel generated")