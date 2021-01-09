Contains SpringBoard learning unit 5.5.4

Work is under the base directory : mywork

scrapy_mini_project/spider/quotes_spider.py    - generates the json extract css-scraper-results.json using css selector
scrapy_mini_project/spider/quotes_spider_xpath.py    - generates the json extract xpath-scraper-results.json using xpath expressions

Process_data.ipynb - contain code to load the json scraped data into SQLite3 DB Unit554.db

Unit554.db - contains the SQLite3 Database with all the data.

:
Lesson learnt:
==============
start_urls option does not prevent a page from being rescanned it that page was already scanned through link follows