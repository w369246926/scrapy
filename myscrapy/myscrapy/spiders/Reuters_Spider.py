import scrapy

class ReutersSpider(scrapy.Spider):
    name = "reuters"
    start_urls = ['https://www.reuters.com/']

    def parse(self, response):
        for article in response.css('article.story'):
            title = article.css('h3.story-title::text').get().strip()
            link = response.urljoin(article.css('a::attr(href)').get())
            yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.StandardArticleBody_body p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
