import httpx
import asyncio
from typing import Optional, List
from bs4 import BeautifulSoup


class Quote:
    text: str
    author: str

    def __init__(self, *, text, author):
        self.text = text
        self.author = author


async def get_page_html(url) -> Optional[str]:
    """
    HTTP Request to the website
    """

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            html = response.text
            return html
    except Exception as e:
        print(e)
        return None


async def web_scraping(url) -> List[Quote]:
    print("[INFO] Web scraping...")
    html = await get_page_html(url)
    # Getting page info
    soup_page = BeautifulSoup(html, "html.parser")
    quotes = soup_page.find_all("div", {"class": "quotes"})
    quotes_list: List = []

    for quote in quotes:
        paragrah = quote.find("p", {"class": "aquote"})
        quote_text = paragrah.text.strip()
        author = quote.find("p", {"class": "author"})
        author_text = author.text.strip()
        quote_obj = Quote(text=quote_text, author=author_text)
        quotes_list.append(quote_obj)
    return quotes_list


if __name__ == "__main__":
    url = "https://bluelimelearning.github.io/my-fav-quotes/"
    quotes = asyncio.run(web_scraping(url))
    for quote in quotes:
        print(f'"{quote.text}", {quote.author}')
