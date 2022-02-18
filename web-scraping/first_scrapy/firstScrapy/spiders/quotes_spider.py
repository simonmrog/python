import scrapy
from typing import List, Dict
from firstScrapy.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name: str = "quotes"
    start_urls: List[str] = ["https://bluelimelearning.github.io/my-fav-quotes/"]

    def parse(self, response) -> Dict[str, str]:
        quotes = response.css("div.quotes")
        for quote in quotes:
            quote_text = quote.css("p.aquote::text").extract_first().strip()
            author_text = quote.css("p.author::text").extract_first().strip()
            quote_obj = QuoteItem(
                text=quote_text,
                author=author_text,
            )
            yield quote_obj.dict()
