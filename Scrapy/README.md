# Scrapy Tutorial
Before scraping, we will have to set up a new project by doing

`scrapy startproject tutorial`


This will create a tutorial with the following contents:

`
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
`

## My First Spider
Spiders are classes that you define that Scrapy uses to scrape information from a website. They must subclass `scrapy.Spider` and define the initial requests to make, optionally how to follow links in the pages, and how to parse the downloaded page content to extract data.

Have a look at `quotes_spider.py` under the `tutorial/spiders` directory.

## How to run our spider

To put our spider to work, go to the project's top level directory and run
`scrapy crawl quotes`

Now, check the fles in the current directory: 2 new files named *quotes-1.html* and *quotes-2.html* have been created, with the content for the respective URLs.

### What is going on here?
Scrapy schedules the scrapy.Request objects, returned by the 'start_requests' method. Upon receiving a response for each one, it instantiates `Response` objects and calls the callback method `parse`, passing the response as an argument.

## A shortcut to the start_requests method.
Instead of implementing `start_requests`, you can just define a `start_urls` class attribute with a list of URLs. This list will then be used by the default implementation of `start_requests` to create the initial requests for your spider.

The `parse` method will be called to handle each of the requests for those URLs, even though we haven't explicitly told Scrapy to do so (parse is the callback method by default).

## Extracting data

Let's use [Scrapy shell](https://doc.scrapy.org/en/latest/topics/shell.html#topics-shell):

`scrapy shell 'http://quotes.toscrape.com/page/1'` and then `response.css('title')`. This will look for tags named 'title' in the response, and will return them as a list.

`>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]`

To extract the text from the title above, you can do:

`response.css('title::text').extract()`

and if you use `.extract_first()`, it will get the first item on that list.

`>>> response.css('title::text').extract_first()
'Quotes to Scrape'`

Remember that using `extract_first()` avoids an IndexError when it doesn't find any element matching the selection.

Besides the `extract()` method, we can use `re()` to extract using *regular expressions*.

`>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']`

In order to find the proper CSS selector to use, you might find useful opening the response page from the shell in your web browser using `view(response)`. It will open the web browser with the website.

## XPath: a brief intro
Besides CSS, Scrapy selectors also support using XPath expressions:

`response.xpath('//title')`

XPath expressions are very powerful, and the foundation of Scrapy Selectors. They are so because besides navigating the structure, it can also look at the content. Using XPath we are able to select things like *select the link that contains the text "Next Page"*. This makes XPath very fitting to the task of scraping, and we encourage to learn [XPath](https://doc.scrapy.org/en/latest/topics/selectors.html#topics-selectors), with this [tutorial](http://zvon.org/comp/r/tut-XPath_1.html) and this [one](http://plasmasturm.org/log/xpath101/).

## Extracting quotes and authors

Each quote in quotes.toscrape.com is represented by HTML elements that look like this:

```html
<div class="quote">
    <span class="text">“The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.”</span>
    <span>
        by <small class="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>
```

We get a list of selectors for the quote HTML elements with:

`response.css("div.quote")`

We can do, then, `quote = response.css("div.quote")[0]` as an example, and extract title, author and the tags from that quote using the quote object we have just created:

```
title = quote.css("span.text::text").extract_first()
author = quote.css("small.author::text").extract_first()
tags = quote.css("div.tags a.tag::text").extract()
```

Having figured out how to extract each bit, we can now iterate over all the quotes elements and put them together into a dictionary:

```python
for quote in response.css("div.quote"):
    text = quote.css("span.text::text").extract_first()
    author = quote.css("small.author::text").extract_first()
    tags = quote.css("div.tags a.tag::text").extract()
    print(dict(text=text, author=author, tags=tags))
```

## Extracting Data in the Spider

Until now, the spider doesn't extract any data in particular, but only saves the whole HTML page to a local file. Let's integrate the extraction logic used above into it.

A Scrapy spider typically generates many dictionaries containing the data extracted from the page. To do that, we use `yield` in the callback, as used in quotes_spider:

```python
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
```


If we run the spider again using `scrapy crawl quotes`, it will output the extracted data with the log.

## Storing the scraped data

The simplest way to store the scraped data is by using [Feed exports](https://doc.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports), by doing

`scrapy crawl quotes -o quotes.json`.

Be aware that running the command again will append the new quotes to the file instead of overwritting.

## Following links

Instead of just scraping, let's say we want quotes from all pages in the website. Now that we now how to extract data from pages, let's see how to follow links from them.

First, we need to extract the link to the page we want to follow. Examining our page, we can see there is a link to the next page:

```html
<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>
```

we can try extracting it in the shell:
```
>>>response.css('li.next a').extract_first()
'<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'
```

And by doing `esponse.css('li.next a::attr(href)').extract_first()`, we obtain the link to the following page.

We can add that logic to our spider by doing:

```python
def parse(self, response):
      """Callback method."""
      # ...

      # Follow the next page
      next_page = response.css('li.next a::attr(href)').extract_first()
      if next_page is not None:
          next_page = response.urljoin(next_page)
          yield scrapy.Request(next_page, callback=self.parse)
```


What we can also do is the following, a much simpler way:

```python
def parse(self, response):
      """Callback method."""
      # ...

      # Follow the next page
      next_page = response.css('li.next a::attr(href)').extract_first()
      if next_page is not None:
          yield response.follow(next_page, callback=self.parse)
```

By using response.follow, we don't need to call urljoin.

You can also pass a selector to response.follow with the necessary attributes:

```python
for href in response.css('li.next a::attr(href)'):
    yield response.follow(href, callback=self.parse)
```

And for `<a>` tags there is a shortcut:

```python
for a in response.css('li.next a'):
  yield response.follow(a, callback=self.parse)
```
