import requests
from bs4 import BeautifulSoup
from config import HEADERS

def scrape_careerbeacon():
    url = "https://www.careerbeacon.com/en/search/jobs-in-new-brunswick/technology"
    r = requests.get(url, headers=HEADERS, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []

    for job in soup.select(".job"):
        jobs.append({
            "title": job.select_one(".job-title").get_text(strip=True),
            "company": job.select_one(".company").get_text(strip=True),
            "location": "New Brunswick",
            "summary": job.select_one(".summary").get_text(strip=True),
            "url": job.a["href"],
            "source": "CareerBeacon"
        })

    return jobs
