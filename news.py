import requests
from bs4 import BeautifulSoup

url="https://www.bbc.com/news"
response=requests.get(url)

if response.status_code==200:
    soup=BeautifulSoup(response.content, "html.parser")
    headlines=soup.find_all("h2")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        saved = set() #for unique headlines 
        for headline in headlines:
            text=headline.get_text(strip=True)
            
            if text:
                file.write(text + "\n")
                saved.add(text)
        print("Headline successfully saved in headlines.txt")
    
else:
    print("Failed to retrive the news. status code:", response.status_code)