from bs4 import BeautifulSoup
import requests


def save_file():
    with open('avito vakansii IT.txt', 'a', encoding="utf-8") as file:
        file.write(f"\n------------------------------\n\n"
              f"{elem['title']}\n"
              f"{elem['price']}\n"
              f"{elem['time']}\n"
              f"Link: {elem['link']}")


def parse():
    URL = 'https://www.avito.ru/moskva/vakansii/it_internet_telekom-ASgBAgICAUSOC_SdAQ?cd=1'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_ = 'iva-item-content-UnQQ4')
    elems = []

    for item in items:
        elems.append({
            'title': item.find('a', class_ = 'link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes').get_text(strip=True),
            'price': item.find('span', class_ = 'price-text-E1Y7h text-text-LurtD text-size-s-BxGpL').get_text(strip=True),
            'time': item.find('div', class_ = 'iva-item-text-_s_vh text-text-LurtD text-size-s-BxGpL').get_text(strip=True),
            'link': 'https://www.avito.ru' + item.find('a', class_ = 'link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes').get('href')
        })
    global elem
    for elem in elems:
        print(f"\n------------------------------\n\n"
              f"{elem['title']}\n"
              f"{elem['price']}\n"
              f"{elem['time']}\n"
              f"Link: {elem['link']}")
        save_file()


parse()

