import schedule
import time
from main import run

schedule.every().monday.at("06:00").do(run)

while True:
    schedule.run_pending()
    time.sleep(60)
