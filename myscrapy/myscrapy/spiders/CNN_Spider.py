import scrapy

class CNNSpider(scrapy.Spider):
    name = "cnn"
    start_urls = ['https://edition.cnn.com/']

    def parse(self, response):
        for article in response.css('h3.cd__headline'):
            title = article.css('a::text').get().strip()
            link = response.urljoin(article.css('a::attr(href)').get())
            yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.l-container p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
