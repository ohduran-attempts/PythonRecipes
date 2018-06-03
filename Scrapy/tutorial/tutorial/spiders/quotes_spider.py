import scrapy


class QuotesSpider(scrapy.Spider):
    """
    Quotes Spider.

    name: identifies the Spider (unique within a project).

    start_requests(): must return an iterable of Requests
    (either a list of requests or a generator function), which the Spider
    will begin to crawl from. Subsequent requests will be generated succesively
    from these initial requests.

    parse(): Will handle the response downloaded for each of the requests made.
    The response parameter is an instance of TextResponse that holds the page content
    and has further helpful methods to handle it.
    """

    name = 'quotes'

    def start_requests(self):
        """Start requests method."""
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Callback method."""
        page = response.url.split("/")[-2]  # number of page
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
