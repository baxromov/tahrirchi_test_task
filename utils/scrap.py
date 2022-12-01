import csv
import datetime
from typing import Optional
import requests
from bs4 import BeautifulSoup

from utils.detect_language import DetectLanguage
from collections import Counter


class ScrapFromKunUz:
    URL = 'https://kun.uz'

    def __init__(self) -> Optional[None]:
        self.page = requests.get(self.URL)
        self.latest_news = BeautifulSoup(self.page.content, 'html.parser').find_all('span',
                                                                                    {'class': 'news-lenta__title'})

    @property
    def get_latest_news_urls(self) -> Optional[list]:
        return [item.parent.attrs.get('href') for item in self.latest_news]

    @property
    def get_dataset(self) -> Optional[list]:
        hrefs = self.get_latest_news_urls
        data = list()
        for item in hrefs:
            datum = dict()
            url = self.URL + item
            page = requests.get(url)
            news = BeautifulSoup(page.content, 'html.parser').find_all('p', {'dir': 'auto'})
            news_text = [item.text for item in news]
            datum['source_url'] = url
            datum['access_datetime'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            if len(news_text) != 0:
                new_text = " ".join(news_text)
                counter = Counter(new_text.split())
                datum['content'] = new_text
                n = new_text.find('.')
                datum['word'] = new_text[:n + 1]
                datum['most_common'] = f'{counter.most_common()[0][0]} - {counter.most_common()[0][1]}'
                data.append(datum)
        return data

    @property
    def dataset(self) -> Optional[list]:
        res = list()
        data = self.get_dataset
        for item in data:
            if DetectLanguage(item.get('content')[:255]).is_language():
                res.append(item)
        return res[:3]

    def get_csv(self) -> Optional[None]:
        keys = self.dataset[0].keys()
        with open('people.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.dataset)
        print('Status OK')
