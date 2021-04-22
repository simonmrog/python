# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    text: str = scrapy.Field()
    author: str = scrapy.Field()

    def dict(self):
        return {
            "text": self["text"],
            "author": self["author"],
        }
