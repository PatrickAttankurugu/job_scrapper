from scrapers import ghana_sites, dubai_sites, remote_sites
from data_handler import save_data

# Call the scraper for each site type and collect the results
ghana_jobs = ghana_sites.scrape_jobs()
dubai_jobs = dubai_sites.scrape_jobs()
remote_jobs = remote_sites.scrape_jobs()

# Combine all the job listings into one list
all_jobs = ghana_jobs + dubai_jobs + remote_jobs

# Save the data to a JSON file
save_data(all_jobs, 'data/jobs.json')
