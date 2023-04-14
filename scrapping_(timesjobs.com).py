from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit'
                    '&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(page, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_="joblist-comp-name").text.strip()
    location = job.find('span').get('title')
    skills = job.find('span', class_='srp-skills').text.strip().split(',')

    print(f"Company Name: {company_name}")
    print(f"Location: {location}")
    print(f"Skills: {skills}")
    print()
    #print(f"Company Name: {company_name}\nLocation: {location}\nSkills: {skills}\n{'-'*50}\n")
