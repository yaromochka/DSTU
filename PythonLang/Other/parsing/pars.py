import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {'User-Agent':
           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729) Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def download(url):
    resp = requests.get(url, stream=True)
    r = open('C:\\Users\\Ромочка\\Desktop\\images\\' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024 * 1024):
        r.write(value)
    r.close()


def get_url():
    for j in range(1, 8):

        url = 'https://scrapingclub.com/exercise/list_basic/?page=' + str(j)

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml') # 'html.parser'

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url


def array():
    for card_url in get_url():

        resp = requests.get(card_url, headers=headers)
        sleep(1)
        sp = BeautifulSoup(resp.text, 'lxml')

        dt = sp.find('div', class_='card mt-4 my-4')
        name = dt.find('h3', class_='card-title').text.replace('\n', '')
        price = dt.find('div', class_='card-body').find('h4').text.replace('\n', '')
        desc = dt.find('p', class_='card-text').text.replace('\n', '')
        img_url = 'https://scrapingclub.com' + dt.find('img', class_='card-img-top img-fluid').get('src')
        download(img_url)
        yield name, price, img_url, desc
