import requests
from bs4 import BeautifulSoup
from config import HEADERS

def scrape_jobbank():
    url = (
        "https://www.jobbank.gc.ca/jobsearch/jobsearch"
        "?searchstring=information+technology"
        "&locationstring=New+Brunswick"
    )

    r = requests.get(url, headers=HEADERS, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = []

    for job in soup.select(".resultJobItem"):
        try:
            jobs.append({
                "title": job.select_one("h3").get_text(strip=True),
                "company": job.select_one(".business-name").get_text(strip=True),
                "location": job.select_one(".location").get_text(strip=True),
                "summary": job.select_one(".job-posting-summary").get_text(strip=True),
                "url": "https://www.jobbank.gc.ca" + job.a["href"],
                "source": "Job Bank"
            })
        except AttributeError:
            continue

    return jobs
