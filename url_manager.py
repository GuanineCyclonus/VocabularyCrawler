class UrlManager():
    def __init__(self):
        self.urls = set()
        self.urls_visited = set()

    def add_url(self, url):
        if len(url) == 0 or url is None:
            return
        if url in self.urls or url in self.urls_visited:
            return
        self.urls.add(url)
    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)
    
    def get_url(self):
        if len(self.urls) == 0:
            return None
        url = self.urls.pop()
        self.urls_visited.add(url)
        return url
    
    def has_url(self, url):
        return url in self.urls

    def get_url_count(self):
        return len(self.urls)

    def get_all_urls(self):
        return self.urls