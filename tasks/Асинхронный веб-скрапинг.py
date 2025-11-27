# Ваш коллега-тестировщик скинул вам список страниц, которые его программа считает проблемными. Ваша задача — написать асинхронный код, который обработает все эти страницы и соберёт с них данные, тем самым доказав ему, что страницы в полном порядке. Все числа со страниц необходимо просуммировать для выявления возможных отклонений.

# Сервер, с которого вы будете собирать данные, не очень мощный и рассчитан только на 75 запросов от клиентов в секунду. По этой причине вам необходимо использовать семафор для ограничения количества одновременных запросов, чтобы избежать постоянных разрывов.

# Файл problem_pages.txt содержит список проблемных страниц, каждая из которых указана на новой строке. Эти строки представляют собой имена страниц, которые нужно будет использовать для формирования полных URL-адресов.

# Скачать файл: https://asyncio.ru/zadachi/2/problem_pages.txt

# Пример содержимого файла:
10275454
1046410
10660263
# Для каждого числа из файла problem_pages.txt, необходимо сформировать полный URL-адрес, добавив к нему базовый URL и расширение .html.
# Если имя страницы в файле — 10275454, то полный URL будет: https://asyncio.ru/zadachi/2/html/10275454.html
# Каждая страница содержит тег <p> с id='number', в котором находится число. Это число нужно извлечь и добавить к общей сумме. Ваша задача — суммировать все числа со всех страниц находящихся в файле.

# ссылка на задачу - https://stepik.org/lesson/1075354/step/3?unit=1085452

import aiohttp
import asyncio
from aiohttp.client import ClientResponse
from bs4 import BeautifulSoup
import aiofiles

async def scan_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                p_tags = soup.find('p', id='number').text
                return p_tags

async def main():
    results = []
    semaphore = asyncio.Semaphore(75)
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(fr'C:\Users\Lenovo\Dev\asyncio\11\11.9.3.txt') as file:
            page_numbers = await file.readlines()
            tasks = [scan_url(fr'https://asyncio.ru/zadachi/2/html/{number}.html', semaphore) for number in page_numbers]
            result = await asyncio.gather(*tasks, return_exceptions=True)
            results.extend(result)
    print(sum(int(result) for result in results if isinstance(result, str)))

asyncio.run(main())