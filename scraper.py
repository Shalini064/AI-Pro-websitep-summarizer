import requests
from bs4 import BeautifulSoup

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

def fetch_website_content(url):
    #Add schema if the user forgot it
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url, headers=HEADER,timeout=15)
        response.raise_for_status()  # Raise an error for bad responses
          
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'

        for tag in soup(["script", "style","nav","footer","header","img","input","button","svg","noscript"]):
            tag.decompose()
                
        text = soup.get_text(separator='\n', strip=True)
        return f"Website Title: {title}\n\nExtracted Text:\n{text}"

    except requests.exceptions.RequestException as e:
        return f"Error fetching the website content: {e}"
                


