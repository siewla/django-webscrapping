import requests
from bs4 import BeautifulSoup

url = "https://sg.jobsdb.com/j?sp=search&q=developer&l=singapore"

page = requests.get(url)
# print(page.content)

parsed_html = BeautifulSoup(page.content, "html.parser")
# print(parsed_html)

list_of_jobs = parsed_html.find_all("div", class_="job-container")
# print(list_of_jobs)

final_list_of_jobs = []

for job in list_of_jobs:
    title = job.find("h3", class_="job-title").text
    # print(title)
    company_name = job.find("span", class_="job-company").text
    # print(company_name)
    job_location = job.find("span", class_="job-location").text
    # print(job_location)
    link = "https://sg.jobsdb.com" + job.find('a').get('href')
    # print(link)

    job_details = {"title": title, "company_name": company_name,
                   "job_location": job_location, "link": link}
    # print(job_details)

    final_list_of_jobs.append(job_details)

# print(final_list_of_jobs)
