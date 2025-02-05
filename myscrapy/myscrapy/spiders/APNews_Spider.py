import scrapy

class APNewsSpider(scrapy.Spider):
    name = "apnews"
    start_urls = ['https://apnews.com/']

    def parse(self, response):
        for article in response.css('div.FeedCard'):
            title = article.css('h1::text').get().strip()
            link = response.urljoin(article.css('a::attr(href)').get())
            yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.Article p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
