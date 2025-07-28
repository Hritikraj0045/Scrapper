# ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from scheduler import ScraperJob
from config import CSV_OUTPUT, DEFAULT_INTERVAL

class AppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Data Scraper")
        self.job = None

        self.build_form()
        self.build_log_box()

    def build_form(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.pack()

        ttk.Label(frm, text="Website URL").grid(row=0, column=0)
        self.url_entry = ttk.Entry(frm, width=40)
        self.url_entry.grid(row=0, column=1)

        ttk.Label(frm, text="Data Label").grid(row=1, column=0)
        self.label_entry = ttk.Entry(frm, width=40)
        self.label_entry.grid(row=1, column=1)

        ttk.Label(frm, text="Div ID").grid(row=2, column=0)
        self.id_entry = ttk.Entry(frm, width=40)
        self.id_entry.grid(row=2, column=1)

        ttk.Label(frm, text="Start Time (HH:MM)").grid(row=3, column=0)
        self.start_entry = ttk.Entry(frm, width=40)
        self.start_entry.grid(row=3, column=1)

        ttk.Label(frm, text="End Time (HH:MM)").grid(row=4, column=0)
        self.end_entry = ttk.Entry(frm, width=40)
        self.end_entry.grid(row=4, column=1)

        ttk.Button(frm, text="Start", command=self.start_job).grid(row=5, column=0)
        ttk.Button(frm, text="Stop", command=self.stop_job).grid(row=5, column=1)

    def build_log_box(self):
        self.log_box = tk.Text(self.root, height=10, width=80)
        self.log_box.pack(padx=10, pady=10)

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

    def start_job(self):
        try:
            start_time = datetime.strptime(self.start_entry.get(), "%H:%M").time()
            end_time = datetime.strptime(self.end_entry.get(), "%H:%M").time()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please use HH:MM format.")
            return

        self.job = ScraperJob(
            url=self.url_entry.get(),
            element_id=self.id_entry.get(),
            label=self.label_entry.get(),
            start=start_time,
            end=end_time,
            interval=DEFAULT_INTERVAL,
            csv_path=CSV_OUTPUT,
            ui_callback=self.log
        )
        self.job.start_job()
        self.log("Job started.")

    def stop_job(self):
        if self.job:
            self.job.stop()
            self.log("Job stopped.")
