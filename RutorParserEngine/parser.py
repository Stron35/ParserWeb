from bs4 import BeautifulSoup
import requests
import re

# http://rutor.info/browse/


def get_html(url):
    return requests.get(url).text

def get_page_data(html):
    #добавить ещё размер, сидеров и личеров
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr', {'class':['gai', 'tum']})
    data = {}
    for tr in trs:
        try:
            title = tr.find('a', href=re.compile('/torrent/')).text.strip()
        except:
            continue

        try:
            if 'torrent' not in tr.find('a', href=re.compile('/torrent/')).get('href'):
                continue
            else:
                link = 'http://rutor.info' + tr.find('a', href=re.compile('/torrent/')).get('href')
        except:
            continue

        try:
            if 'magnet' not in tr.find('a', href=re.compile('magnet')).get('href'):
                continue

            else:
                magnet_link = tr.find('a', href=re.compile('magnet')).get('href')
        except:
            continue
        try:
            size = tr.find('td', text = re.compile('B')).text.strip()
        except:
            continue
        try:
            sid = tr.find('span', class_='green').text.strip()
        except:
            continue
        try:
            pir = tr.find('span', class_='red').text.strip()
        except:
            continue
        # info = {'link':link, 'magnet_link': magnet_link, 'size': size, 'sid':sid, 'pir': pir}
        info ={'link':link, 'magnet_link': magnet_link, 'size': size, 'sid':sid, 'pir': pir }
        data[title] = info
    return data
    # print(data)

def main_parser(query):
    #http://rutor.info/search/Warcraft
    base_url = 'http://rutor.info/search/'
    query_set = '%20'.join(query.split())
    url = base_url + query_set
    html = get_html(url)
    data = get_page_data(html)
    return data


if __name__ == '__main__':
    query = 'Warcraft'
    main_parser(query)