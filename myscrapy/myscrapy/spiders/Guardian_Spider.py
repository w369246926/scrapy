import scrapy

class GuardianSpider(scrapy.Spider):
    name = "guardian"
    start_urls = ['https://www.theguardian.com/international']

    def parse(self, response):
        for article in response.css('div.fc-item__container'):
            title = article.css('a.js-headline-text::text').get().strip()
            link = response.urljoin(article.css('a.js-headline-text::attr(href)').get())
            yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.content__article-body p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
