import scrapy

class AlJazeeraSpider(scrapy.Spider):
    name = "aljazeera"
    start_urls = ['https://www.aljazeera.com/']

    def parse(self, response):
        for article in response.css('div.gs-c-promo'):
            title = article.css('h3 a::text').get()
            if title:
                title = title.strip()
                link = response.urljoin(article.css('h3 a::attr(href)').get())
                yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.article-body p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
