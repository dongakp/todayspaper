import json
import re

try:
    with open('papersInfo.json','r') as f:
        papers = json.load(f)
except FileNotFoundError:
    papers = []

def paperIncluding(keyWord):
    selectedPapers=[]
    for paper in papers:
        if re.search(keyWord,paper['title'],re.IGNORECASE) is not None or\
            re.search(keyWord,paper['abstract'],re.IGNORECASE) is not None:
            selectedPapers.append(paper)
    return selectedPapers

def titleOf(keyWord):
    selectedPapers=[]
    for paper in papers:
        if re.search(keyWord,paper['title'],re.IGNORECASE) is not None:
            selectedPapers.append(paper)
    return selectedPapers

def abstractOf(keyWord):
    selectedPapers=[]
    for paper in papers:
        if re.search(keyWord,paper['abstract'],re.IGNORECASE) is not None:
            selectedPapers.append(paper)
    return selectedPapers

def authorOf(keyWord):
    selectedPapers=[]
    for paper in papers:
        for author in paper['authors']:
            if re.search(keyWord,author,re.IGNORECASE) is not None:
                selectedPapers.append(paper)
                break
    return selectedPapers