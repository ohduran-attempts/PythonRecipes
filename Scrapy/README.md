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
