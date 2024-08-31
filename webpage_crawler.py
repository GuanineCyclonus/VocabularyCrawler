import requests
import url_manager
import re
from bs4 import BeautifulSoup

pattern = re.compile(r'托福词汇表.+')
pattern_url = re.compile(r'http://toefl.xdf.cn/\d{6}/\d{8}.html')

def crawl_webpage(url):
    UrlManager = url_manager.UrlManager()
    UrlManager.add_url(url)
    vocabularies = set()
    while UrlManager.get_url_count() > 0:
        url = UrlManager.get_url()
        # print(f"Crawling webpage: {url}")

        # Send a GET request to the webpage
        response = requests.get(url, timeout=5)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')

            div_node = soup.find('div', class_='xdf_content_detail')
            
            if div_node is None:
                print(f"Failed to find div node in webpage: {url}")
                continue

            links = div_node.find_all('a')
            
            for link in links:
                if link['href'] in UrlManager.urls_visited:
                    continue
                print(link.name, link['href'], link.get_text())
                if pattern.match(link.get_text()):
                    # print(f"Found a link with the desired text: {link.get_text()}")
                    vocabularies.add(link['href'])
                if pattern_url.match(link['href']):
                    UrlManager.add_url(link['href'])
            # Extract the desired information from the webpage    
        else:
            print(f"Failed to crawl webpage: {url}")

    print(f"Found {len(vocabularies)} vocabularies")
    for vocabulary_webpage in vocabularies:
        print(vocabulary_webpage)
    with open('./--urls.txt', 'w') as f:
        for vocabulary_webpage in vocabularies:
            f.write(vocabulary_webpage + '\n')
    
# Example usage
crawl_webpage('https://toefl.xdf.cn/202110/11225216.html')