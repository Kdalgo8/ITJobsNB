import pandas as pd
from scrapers.jobbank import scrape_jobbank
from scrapers.careerbeacon import scrape_careerbeacon
from scrapers.nbjobs import scrape_nbjobs
from utils.categorizer import categorize
from utils.deduplicator import deduplicate
from config import OUTPUT_FILE

def run():
    jobs = []
    jobs.extend(scrape_jobbank())
    jobs.extend(scrape_careerbeacon())
    jobs.extend(scrape_nbjobs())

    jobs = deduplicate(jobs)

    for job in jobs:
        job["category"] = categorize(job["title"], job["summary"])

    df = pd.DataFrame(jobs)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(df)} jobs to {OUTPUT_FILE}")

if __name__ == "__main__":
    run()
