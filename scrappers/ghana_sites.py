import requests
from bs4 import BeautifulSoup
import time
import json

def scrape_jobs(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = soup.find_all('div', class_='job') # Replace 'div' and 'job' with actual HTML tag and class

    job_list = []
    for job in jobs:
        title = job.find('h2').text # Replace 'h2' with actual HTML tag for job title
        company = job.find('div', class_='company').text # Replace 'div' and 'company' with actual HTML tag for company
        location = job.find('div', class_='location').text # Replace 'div' and 'location' with actual HTML tag for location
        link = job.find('a')['href'] # Replace 'a' with actual HTML tag for job link

        job_dict = {
            "Title": title,
            "Company": company,
            "Location": location,
            "Link": link
        }

        job_list.append(job_dict)

    return job_list

def scrape_all_pages(base_url, num_pages):
    all_jobs = []

    for i in range(1, num_pages + 1):
        print(f"Scraping page {i}")
        all_jobs.extend(scrape_jobs(f"{base_url}/page/{i}")) # Update the URL as per the actual pagination URL of the website
        time.sleep(1) # Delay for 1 second

    with open('jobs.json', 'w') as f:
        json.dump(all_jobs, f, indent=4)

    print("Scraped all jobs and saved to jobs.json")

base_url_jobberman = "https://www.jobberman.com.gh/jobs" # Replace with actual base URL
num_pages_jobberman = 10 # Replace with the actual number of pages you want to scrape for Jobberman

base_url_jobsinghana = "https://www.jobsinghana.com/jobs" # Replace with actual base URL
num_pages_jobsinghana = 10 # Replace with the actual number of pages you want to scrape for JobsInGhana

print("Scraping Jobberman")
scrape_all_pages(base_url_jobberman, num_pages_jobberman)
time.sleep(5) # Delay for 5 seconds between scraping different websites

print("Scraping JobsInGhana")
scrape_all_pages(base_url_jobsinghana, num_pages_jobsinghana)
