import os

from bs4 import BeautifulSoup
from django.contrib.sites import requests

PATH_MODULE = os.path.abspath(__file__)
ROOT_DIR = os.path.dirname(os.path.dirname(PATH_MODULE))
DATA_DIR = os.path.join(ROOT_DIR, 'data')

print(PATH_MODULE)
print(ROOT_DIR)
print(DATA_DIR)


class MelonCrawler:
    def artist_search(self, q):
        url ='http://www.melon.com/search/artist/index.htm'
        params = {
            'q':q,
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        info_list = soup.select('form#frm_defaultList table > tbody > li')

        result = []
        for core_info in info_list:
            artist_id = 'melon.link.goArtistDetail('여기')
            artist = 'title='바로 뒤
            url_img_cover = img onerror > src="주소"
