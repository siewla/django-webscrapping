from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def index(request):
    final_list_of_jobs = []
    if request.method == 'POST':
        # print(request.POST['search'])
        url = f"https://sg.jobsdb.com/j?sp=search&q={request.POST['search']}&l=singapore"
        page = requests.get(url)
        # print(page.content)

        parsed_html = BeautifulSoup(page.content, "html.parser")
        # print(parsed_html)

        list_of_jobs = parsed_html.find_all("div", class_="job-container")
        # print(list_of_jobs)

        for job in list_of_jobs:
            title = job.find("h3", class_="job-title").text
            # print(title)
            company_name = ""
            if job.find("span", class_="job-company"):
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


    return render(request, "jobsdb/index.html", {"jobs":final_list_of_jobs})


def show(request, name):
    return render(request, "jobsdb/show.html", {"from_url": name})
