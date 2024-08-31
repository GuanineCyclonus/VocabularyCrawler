import requests
import url_manager
import re
from bs4 import BeautifulSoup

pattern = re.compile(r'托福词汇表.+')
pattern_url = re.compile(r'http://toefl.xdf.cn/\d{6}/\d{8}.html')

def crawl_vocabularies():
    UrlManager = url_manager.UrlManager()
    vocabularies = set()
    with open('./urls.txt', 'r') as f:
        urls = f.readlines()
        for url in urls:
            UrlManager.add_url("https" + url[4:-1])

    while UrlManager.get_url_count() > 0:
        url = UrlManager.get_url()
        print(f"Crawling vocabulary webpage: {url}")

        # Send a GET request to the webpage
        response = requests.get(url, timeout=5)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')

            # table_node = soup.find('table')
            
            # if table_node is None:
            #     print(f"Failed to find table node in webpage: {url}")
            #     continue
            # else:
            #     print(f"Found table node in webpage: {url}")
            #     print(table_node)
            div_node = soup.find('div', class_='xdf_content_detail')
            
            if div_node is None:
                # print(f"Failed to find div node in webpage: {url}")
                continue
            else:
                # print(f"Found div node in webpage: {url}")
                td_node = div_node.find_all('td')
                for node in td_node:
                    with open('./result.txt', 'a') as f:
                        f.write(node.get_text())
            # Extract the desired information from the webpage    
        else:
            print(f"Failed to crawl webpage: {url}")
            print(response.status_code)
    
# Example usage
crawl_vocabularies()