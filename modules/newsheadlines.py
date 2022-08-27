import requests
from bs4 import BeautifulSoup
  
LENGTH = 26

def headlines():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch']
    
    return ' | '.join(x.text.strip() for x in list(dict.fromkeys(headlines)) if x.text.strip() not in unwanted)
