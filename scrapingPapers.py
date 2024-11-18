import requests
from bs4 import BeautifulSoup
import json

def scrap():
    # requesting new papers
    response = requests.get('https://arxiv.org/list/astro-ph/new')
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print(response.status_code)

    # parsing paper info
    titles = soup.select('.list-title.mathjax')
    authors = soup.select('.list-authors')
    subjects = soup.select('.primary-subject')
    abstracts = soup.select('p.mathjax')
    arXivIDs = soup.select('a[title~="Abstract"]')

    # saving the info
    metaDatas=[]
    for i in range(len(titles)):
        arXivID = arXivIDs[i].get_text()
        IDstart = arXivID.find('arXiv')+6
        IDend = arXivID[IDstart:].find('\n') + IDstart
        metaData = {
            'ID':arXivID[IDstart:IDend],
            'title':titles[i].get_text(),
            'authors':authors[i].get_text().split(','),
            'subject':subjects[i].get_text(),
            'abstract':abstracts[i].get_text()
        }
        metaDatas.append(metaData)
    with open('papersInfo.json','w') as f:
        json.dump(metaDatas,f)
    return