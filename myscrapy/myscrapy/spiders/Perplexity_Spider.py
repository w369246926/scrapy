import scrapy
from scrapy_selenium import SeleniumRequest



class PerplexitySpider(scrapy.Spider):
    name = "perplexity"
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'https://www.perplexity.ai/',  # Add the referer if needed
            'Origin': 'https://www.perplexity.ai',   # Some sites check the origin
        }
        yield SeleniumRequest(
            url='https://www.perplexity.ai/discover',
            callback=self.parse,
            headers=headers
        )

    def parse(self, response):
        # 假设新闻标题和链接在某个特定的 div 中
        for article in response.css('a.group/card block h-full outline-none'):  # 根据页面的实际结构修改这个 CSS 选择器
            title = article.css('h3::text').get()  # 获取标题
            link = article.css('a::attr(href)').get()  # 获取链接

            if title and link:
                yield {
                    'title': title,
                    'link': response.urljoin(link),  # 确保链接是完整的 URL
                }

        # 如果有分页链接，继续抓取更多页面
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
