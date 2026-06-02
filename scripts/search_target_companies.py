import pandas as pd
import requests

OUTPUT_FILE = "data/company_jobs.csv"

TARGET_ROLES = [
    "devops engineer",
    "devsecops engineer",
    "site reliability engineer",
    "sre",
    "platform engineer",
    "cloud engineer",
    "linux administrator",
    "linux engineer",
    "systems administrator",
    "systems engineer",
    "infrastructure engineer",
    "cloud infrastructure engineer",
    "kubernetes engineer"
]

EXCLUDED_KEYWORDS = [
    "manager",
    "director",
    "sales",
    "account executive",
    "product manager",
    "solution architect",
    "solutions architect",
    "marketing",
    "finance",
    "hr",
    "recruiter"
]

GREENHOUSE_COMPANIES = {
    "datadog": "https://boards-api.greenhouse.io/v1/boards/datadog/jobs",
    "cloudflare": "https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs",
    "stripe": "https://boards-api.greenhouse.io/v1/boards/stripe/jobs"
}

jobs = []

for company, url in GREENHOUSE_COMPANIES.items():

    try:
        response = requests.get(url, timeout=30)

        if response.status_code != 200:
            continue

        data = response.json()

        for job in data.get("jobs", []):

            title = job.get("title", "")
            title_lower = title.lower()

            if any(x in title_lower for x in EXCLUDED_KEYWORDS):
                continue

            if not any(x in title_lower for x in TARGET_ROLES):
                continue

            jobs.append({
                "company": company,
                "title": title,
                "location": job.get("location", {}).get("name", ""),
                "job_id": job.get("id"),
                "apply_link": job.get("absolute_url"),
                "source": "target_company"
            })

    except Exception as e:
        print(f"Error {company}: {e}")

df = pd.DataFrame(jobs)

if not df.empty:
    df.drop_duplicates(inplace=True)

df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved {len(df)} jobs")