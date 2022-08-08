import requests
import bs4


class Habr:
    url = 'https://habr.com/ru/all/'

    def __init__(self, headrs):
        self.headers = headrs

    def get_request(self):
        response = requests.get(self.url, headers=self.headers)
        text = response.text
        return text

    def soup_chik(self):
        soup = bs4.BeautifulSoup(self.get_request(), features='html.parser')
        articles = soup.find_all('article', class_='tm-articles-list__item')
        return articles

    def search_in_prewiew(self, key):
        full_data = self.soup_chik()
        for article in full_data:
            words = [word.text.split() for word in article]
            words = {word.strip().lower() for word in words[0]}
            if words & key:
                article_tag_a = article.find(class_='tm-article-snippet')
                href_article = article_tag_a.h2.a.attrs['href']
                article_tag_t = article.find(class_='tm-article-snippet__datetime-published')
                date_article = article_tag_t.time.attrs['title'].split()
                url = 'https://habr.com' + href_article
                print(f'{date_article[0]} {article_tag_a.h2.text}, {url}, Tag: {(words & key).pop()}')

    def search_in_article(self, key):
        full_data = self.soup_chik()
        for article in full_data:
            article_tag_a = article.find(class_='tm-article-snippet')
            href_article = article_tag_a.h2.a.attrs['href']
            url = 'https://habr.com' + href_article
            response = requests.get(url, headers=self.headers).text
            soup = bs4.BeautifulSoup(response, features='html.parser')
            articles = soup.find_all('div', class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
            for artic in articles:
                text = set(artic.text.lower().strip().split())
                if text & key:
                    article_tag_t2 = article.find(class_='tm-article-snippet__datetime-published')
                    date_article = article_tag_t2.time.attrs['title'].split()
                    print(f'{date_article[0]} {article_tag_a.h2.text}, {url}, Tag: {(text & key).pop()}')