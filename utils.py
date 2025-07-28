# utils.py
import csv
import os
from datetime import datetime

def log_to_csv(data_label, value, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data_label, value])

def in_time_range(start, end):
    now = datetime.now().time()
    return start <= now <= end
