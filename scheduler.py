# scheduler.py
import threading
import time
from datetime import datetime

from scraper import init_driver, fetch_data
from utils import log_to_csv, in_time_range

class ScraperJob:
    def __init__(self, url, element_id, label, start, end, interval, csv_path, ui_callback=None):
        self.url = url
        self.element_id = element_id
        self.label = label
        self.start = start
        self.end = end
        self.interval = interval
        self.csv_path = csv_path
        self.ui_callback = ui_callback
        self.running = False
        self.driver = init_driver()

    def start_job(self):
        thread = threading.Thread(target=self.run)
        thread.daemon = True
        thread.start()

    def run(self):
        self.running = True
        while self.running:
            now = datetime.now().time()
            if in_time_range(self.start, self.end):
                value = fetch_data(self.driver, self.url, self.element_id)
                log_to_csv(self.label, value, self.csv_path)
                if self.ui_callback:
                    self.ui_callback(f"[{datetime.now().strftime('%H:%M:%S')}] {self.label}: {value}")
            else:
                if self.ui_callback:
                    self.ui_callback(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting for start time...")
            time.sleep(self.interval)
        self.driver.quit()

    def stop(self):
        self.running = False
