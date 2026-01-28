import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
skills = []
links = []
salary = []
responsibilites = []
date = []
page_num = 0
while True:
    # use requests to fetch url

    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbl&q=python&start={page_num}")

    # save page content/markup
    src = result.content

    # create soup object to parse content
    soup = BeautifulSoup(src , "lxml")

    page_limit = int(soup.find("strong").text)
    
    if (page_num > page_limit // 30):
        print("pages ended , terminate")
        break

    # find the elements containing info we need
    # job titles , job skills ,company names , location names
    job_titles = soup.find_all("h2" , {'class':'css-193uk2c'}) #will hold all the tags that contains all the file we need
    company_names = soup.find_all("a" , {'class':'css-ipsyv7'})
    location_names= soup.find_all("span",{'class':'css-16x61xq'})
    job_skills = soup.find_all("div", class_="css-pkv5jc")  

    for job in job_skills:
        for div in job.find_all("div"):
            text = div.text.strip()

    posted_new = soup.find_all("div", {"class":"css-eg55jf"})
    posted_old = soup.find_all("div", {"class":"css-1jldrig"})
    posted =[*posted_new , *posted_old]
    page_num += 1
    print("page switched")


# loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(job_skills[i].text)
    date_text = posted[i].text.replace("-","").strip()
    date.append(date_text)

for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src , "lxml")
    salaries = soup.find("div", {"class":"css-1ajx53j"})
    if salaries:
        salary.append(salaries.text.strip())
    else:
        salary.append("Not mentioned")
    #Common container classes (update based on current site)
    req_container = soup.find("div", class_="css-1t5f0fr") or \
                    soup.find("section", class_="css-pkv5jc") or \
                    soup.find("div", class_="css-1lqavbg") or \
                    soup.find("div", {"data-testid": "job-requirements"})  # fallback
    
    respon_text = ""
    
    if req_container:
        
        ul = req_container.find("ul")
        if ul:
            for li in ul.find_all("li"):
                respon_text += li.get_text(strip=True) + " | "
        else:
            
            for p in req_container.find_all("p"):
                text = p.get_text(strip=True)
                if text:
                    respon_text += text + " | "
    
    if not respon_text:
        respon_text = "No requirements listed"
    
    responsibilites.append(respon_text.rstrip(" | "))

# create a csv file and fill it with values
file_list = [job_title, company_name, location_name, skills , links ,salary , responsibilites,date]
exported = zip_longest(*file_list)
with open(r'C:\Users\kholo\Downloads\job_details.csv', 'w', newline='', encoding='utf-8') as my_file:
    wr = csv.writer(my_file)
    wr.writerow(["job title", "company name", "location", "skills" , "links" ,"salary" ,"responsibilites","date"])
    wr.writerows(exported)

print("file created successfully")


