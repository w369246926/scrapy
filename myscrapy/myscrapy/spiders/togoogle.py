import scrapy


class TogoogleSpider(scrapy.Spider):
    name = "togoogle"
    allowed_domains = ["news.google.com"]
    start_urls = ["https://news.google.com/home?hl=en-US&gl=US&ceid=US%3Aen"]

    def parse(self, response):
        # 提取新闻标题和链接
        for article in response.css('div.KDoq1'):  # 使用你找到的class名称
            title = article.css('::text').get()  # 获取新闻标题的文本内容
            link = article.css('::attr(href)').get()  # 获取新闻的链接

            # 返回新闻数据
            yield {
                'title': title,
                'link': response.urljoin(link),  # 确保链接是完整的 URL
            }

        # 如果有分页链接，继续抓取更多页面
        next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
