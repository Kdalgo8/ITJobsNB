import requests
from bs4 import BeautifulSoup
from config import HEADERS

def scrape_nbjobs():
    url = "https://www.nbjobs.ca/jobsearch?search=IT"
    r = requests.get(url, headers=HEADERS, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []

    for job in soup.select(".job-listing"):
        jobs.append({
            "title": job.select_one("h3").get_text(strip=True),
            "company": job.select_one(".company").get_text(strip=True),
            "location": "New Brunswick",
            "summary": job.select_one(".description").get_text(strip=True),
            "url": job.a["href"],
            "source": "NBJobs"
        })

    return jobs
