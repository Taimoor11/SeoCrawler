# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import CountryItem


class CountrySpider(CrawlSpider):
    name = 'country'
    start_urls = ['http://example.webscraping.com/']
    #start_urls = [' t/index/{0}'.format(page for page in xrange(1, 277))]
    #start_urls = ["http://example.webscraping.com/places/default/index/{0}".format(x) for x in range(1 , 3)]
    allowed_domains = ['example.webscraping.com']
    rules = (
        Rule(LinkExtractor(allow=r'/index/', deny=r'/user/'), follow=True),
        Rule(LinkExtractor(allow=r'/view/', deny=r'/user/'),
             callback='parse_item')
    )

    def parse_item(self, response):
        print(response.status)
        item = CountryItem()
        name_css = 'tr#places_country__row td.w2p_fw::text'
        item['name'] = response.css(name_css).extract()
        pop_xpath = '//tr[@id="places_population__row"]/td[@class="w2p_fw"]/text()'
        item['population'] = response.xpath(pop_xpath).extract()
        return item
