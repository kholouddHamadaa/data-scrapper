Wuzzuf Job Scraper (Python)
📌 Description

This project is a Python web scraper that collects job listings from Wuzzuf.net for Python-related jobs.
It extracts job details across multiple pages and saves the data into a CSV file for further analysis.

🛠️ Technologies Used

Python

Requests – for sending HTTP requests

BeautifulSoup (bs4) – for parsing HTML content

CSV – for exporting scraped data

itertools.zip_longest – to align extracted lists safely

📊 Data Extracted

For each job posting, the script collects:

Job Title

Company Name

Location

Skills

Job Link

Salary (if available, otherwise "Not mentioned")

Responsibilities / Requirements

Posting Date

🔄 How It Works

Iterates through Wuzzuf job search result pages using pagination.

Extracts job summary information from the search results page.

Visits each job link individually to scrape:

Salary

Job responsibilities / requirements

Stores all extracted data into lists.

Exports the data into a CSV file.

📁 Output

The script generates a CSV file named:

job_details.csv


Located at:

C:\Users\kholo\Downloads\

▶️ How to Run

Install dependencies:

pip install requests beautifulsoup4 lxml


Run the script:

python scraper.py

⚠️ Notes & Limitations

Not all jobs on Wuzzuf include salary information.

Some content may change if Wuzzuf updates its HTML structure.

Excessive requests may result in temporary blocking—use responsibly.

📌 Possible Improvements

Add delay between requests (time.sleep)

Use Selenium for JavaScript-rendered content

Export data to a database instead of CSV

Add logging and exception handling

👩‍💻 Author

Kholoud Hamada
Python Learner & Aspiring Data Engineer