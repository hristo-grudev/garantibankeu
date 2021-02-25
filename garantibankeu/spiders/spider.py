import scrapy

from scrapy.loader import ItemLoader
from ..items import GarantibankeuItem
from itemloaders.processors import TakeFirst


class GarantibankeuSpider(scrapy.Spider):
	name = 'garantibankeu'
	start_urls = ['https://www.garantibank.eu/news/']

	def parse(self, response):
		post_links = response.xpath('//article/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//article//text()[normalize-space() and not(ancestor::h1 | ancestor::p[contains(text(), "Published: ")])]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//time[1]/text()').get()

		item = ItemLoader(item=GarantibankeuItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
