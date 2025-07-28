📊 **Selenium Data Fetcher App**

A Python-based application with a graphical interface that allows users to scrape data dynamically from any website using custom configurations such as website URL, element ID, data label, and scraping time range. It generates a time-stamped CSV report of the fetched data.

🔧 **Features**

✅ Graphical User Interface (Tkinter)
✅ User-defined:
Website URL
HTML element ID (to scrape data from)
Data label/name
Start and end time for continuous scraping
✅ Background data scraping using Selenium
✅ Report generated as a CSV file
✅ Log management for all errors and events
✅ Clean modular codebase

🗂️ **Project Structure**

bash
Copy
Edit
selenium-data-fetcher/
│
├── config.py # Configuration management
├── main.py # Application entry point
├── scraper.py # Selenium logic for fetching data
├── ui.py # User Interface (Tkinter based)
├── logger.py # Logging utility
├── requirements.txt # Dependencies
├── logs/ # Auto-generated logs
├── reports/ # Output CSV files
└── README.md # This file

🖥️ **UI Preview**

The application allows users to:
🔗 Enter a website URL (e.g., https://example.com)
🆔 Specify the HTML element’s ID to fetch
🏷️ Label the data (e.g., “Price”, “Sensex”, “Live Score”)
⏱️ Set Start Time & End Time for scraping
📝 Start scraping & generate report automatically


⚙️ **How It Works**

The user inputs all required fields via GUI.
At the specified start time, Selenium launches in the background.
The app scrapes the value from the given div ID every second.
At the end time, scraping stops, and a report is saved to reports/.
Logs of the entire session are stored in logs/.


🚀 **Getting Started**

1️⃣ _Clone the Repository_

bash
Copy
Edit
git clone https://github.com/yourusername/selenium-data-fetcher.git
cd selenium-data-fetcher

2️⃣ _Install Requirements_

bash
Copy
Edit
pip install -r requirements.txt

3️⃣ _Run the App_

bash
Copy
Edit
python main.py


📦 **Dependencies**

selenium
pandas
tkinter (comes with Python)
datetime
logging

Ensure you have ChromeDriver installed and it matches your Chrome version.


📁 **Output**

CSV Report: Saved in ./reports/ folder with timestamped name.
Logs: Stored in ./logs/ with runtime error info and process trace.


🛠️ **Customization**

You can extend this tool for:
Scraping by class name or XPath
Using headful (non-headless) Chrome for debugging
Multi-element scraping (table scraping, etc.)
Notifications on scraping completion


🤝 **Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss the change.


🧑‍💻 **Author**

Hritik Raj Arya
Data Analyst | Automation Enthusiast | Python Developer


📜 **License**
This project is licensed under the BSE India License.
