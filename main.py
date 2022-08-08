from habr import Habr
from setting import HEADERS


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'IDS', 'Project', 'Debian', 'Самоката', 'Intelligence']


if __name__ == '__main__':
    habr_bot = Habr(HEADERS)
    search_request = set(key.lower() for key in KEYWORDS)
    print('----Search in prewiew----')
    habr_bot.search_in_prewiew(search_request)
    print('----Search in article----')
    habr_bot.search_in_article(search_request)