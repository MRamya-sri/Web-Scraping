#storing the jobs paragraph in text files so created postsTextsaved folder .
from bs4 import BeautifulSoup
import requests
print("put some skill that you're no familiar with")
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
        for index, job in enumerate(jobs):
            published_data = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_data:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
                more_info = job.header.h2.a['href']
                if unfamiliar_skill not in skills:
                    with open(f'postsTextsaved/{index}.txt','w') as f:
                        f.write(f" Company Name: {company_name.strip()} \n")
                        f.write(f" Required Skills : {skills.strip()} \n")
                        f.write(f" More Info: {more_info}")
                    print(f'File save: {index}')


if __name__ == "__main__":
    while True:
        find_jobs()
