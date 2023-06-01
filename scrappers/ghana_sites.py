import requests
from bs4 import BeautifulSoup
import json

class GhanaJobSitesScraper:
    
    def __init__(self):
        self.job_sites = {
            "Jobberman": "https://www.jobberman.com.gh/jobs", # actual URL to be replaced
            "JobsInGhana": "https://www.jobsinghana.com/jobs" # actual URL to be replaced
        }
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        
    def scrape_site(self, site_name):
        url = self.job_sites[site_name]
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_postings = soup.find_all('div', class_='jobposting') # replace 'div' and 'jobposting' with actual HTML tag and class
        
        jobs = []

        for job in job_postings:
            job_title = job.find('a').text.strip() # replace 'a' with actual HTML tag for job title
            company_name = job.find('div', class_='company').text.strip() # replace 'div' and 'company' with actual HTML tag and class for company name
            location = job.find('div', class_='location').text.strip() # replace 'div' and 'location' with actual HTML tag and class for location
            job_url = job.find('a')['href'] # replace 'a' with actual HTML tag for job URL
            
            job_data = {
                'title': job_title,
                'company': company_name,
                'location': location,
                'url': job_url
            }

            jobs.append(job_data)
            
        return jobs

    def scrape_all_sites(self):
        all_jobs = []

        for site in self.job_sites.keys():
            all_jobs.extend(self.scrape_site(site))

        return all_jobs

if __name__ == "__main__":
    scraper = GhanaJobSitesScraper()
    jobs = scraper.scrape_all_sites()
    print(jobs)
