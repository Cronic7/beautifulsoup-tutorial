import requests
from bs4 import BeautifulSoup
URL="https://realpython.github.io/fake-jobs/"
page=requests.get(URL)

 

soup=BeautifulSoup(page.content,"html.parser")


# get element by id
results=soup.find(id="ResultsContainer")
#print(results.prettify())

# get element by html class name

jobs = results.find_all("div",class_="card-content")


for job in jobs:
    title=job.find("h2",class_="title")
    company=job.find("h3",class_="company")
    location=job.find("p",class_="location")
    
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()


 
 
 


