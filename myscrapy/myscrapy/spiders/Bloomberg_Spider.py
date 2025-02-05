# import scrapy
#
# class BloombergSpider(scrapy.Spider):
#     name = "bloomberg"
#     start_urls = ['https://www.bloomberg.com/asia']
#
#     def parse(self, response):
#         for article in response.css('article.story-package-module__story'):
#             title = article.css('h3.story-package-module__headline a::text').get().strip()
#             link = response.urljoin(article.css('h3.story-package-module__headline a::attr(href)').get())
#             yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})
#
#     def parse_article(self, response):
#         title = response.meta
# ::contentReference[oaicite:0]{index=0}
#
# title = response.meta['title']
# link = response.meta['link']
# content = ' '.join(response.css('div.body-copy p::text').getall())
# yield {
#     'title': title,
#     'link': link,
#     'content': content
# }
