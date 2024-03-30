import requests
from bs4 import BeautifulSoup
import urllib.parse

# Функция для выполнения поискового запроса и извлечения ссылок
def extract_links(query):
    url = f"https://www.google.com/search?q={query}&tbs=qdr:w/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.select("a:has(h3)")[:5] # Получаем первые 5 ссылок
        extracted_links = [link["href"] for link in links]
        return extracted_links
    except Exception as e:
        print("Error occurred:", e)
        return []

# Список запросов
queries = [
    "Мероприятия города Перми",
    "События Перми для туристов",
    "События для владельцев малого бизнеса Перми"
]

def parse_page(url):
    try:
        # Получаем HTML-код страницы
        response = requests.get(url)
        # Проверяем успешность запроса
        response.raise_for_status()
        
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Извлекаем весь текст с помощью метода get_text()
        page_text = soup.get_text()
        
        return page_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return ''

# Перебор запросов и запись ссылок в текстовые файлы
for query in queries:
    links = extract_links(query)
    with open(f"{query}.txt", "w", encoding="utf-8") as f:
        for link in links:
            parsed_url = urllib.parse.urlparse(link)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            inner_url = query_params.get('url', [''])[0]
            text = parse_page(inner_url)
            f.write(str(text)+'\n') 