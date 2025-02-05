import scrapy

class BBCSpider(scrapy.Spider):
    name = "bbc"
    start_urls = ['https://www.bbc.com/']

    def parse(self, response):
        for article in response.css('div.media__content'):
            title = article.css('a.media__link::text').get().strip()
            link = response.urljoin(article.css('a.media__link::attr(href)').get())
            yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.story-body__inner p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
