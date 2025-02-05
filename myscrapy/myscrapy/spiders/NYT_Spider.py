import scrapy

class NYTSpider(scrapy.Spider):
    name = "nytimes"
    start_urls = ['https://www.nytimes.com/']

    def parse(self, response):
        for article in response.css('article'):
            title = article.css('h2 a::text').get()
            if title:
                title = title.strip()
                link = response.urljoin(article.css('h2 a::attr(href)').get())
                yield scrapy.Request(link, callback=self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('section[name="articleBody"] p::text').getall())
        yield {
            'title': title,
            'link': link,
            'content': content
        }
