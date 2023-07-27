
# FIRST STEPS

## Scrapy at a glance

data mining, information processing or historical archival
[Web scraping](https://en.wikipedia.org/wiki/Web_scraping)
extract data using APIs
[web crawler](https://en.wikipedia.org/wiki/Web_crawler)

### Walk-through of an example spider

```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

```

run by

```python
scrapy runspider quotes_spider.py -o quotes.jl
```

get result:

```json
{"author": "Jane Austen", "text": "\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"}
{"author": "Steve Martin", "text": "\u201cA day without sunshine is like, you know, night.\u201d"}
{"author": "Garrison Keillor", "text": "\u201cAnyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.\u201d"}
```

Notices:

-start_urls
-parse
-run asynchronously, sending multiple concurrent
-very fast crawls
-can using an auto-throttling

### What else

- selecting and extracting data with XPath and re
- IPython when writing or debugging
- Generating and storing support
- encoding support and auto-detection
- plug in, middlewares, extensions, pipelines
- Wide range of built-in extensions and middlewares
  *cookies and session handling
  *HTTP features like compression, authentication, caching
  *user-agent spoofing
  *robots.txt
  *crawl depth restriction
-Telnet console
-reusable spiders

## Installation

conda
pip Using a virtual environment: pip install scrapy

## Tutorial

[quote site](https://quotes.toscrape.com/)
scrapy shell -> learn how to extract data, trying selectors if exist
XPath vs CSS

### Creating a project

### first Spider

run
start_requests method
Extracting data

### Storing the scraped data

using Feed exports
write an Item Pipeline

### Following links

-link to the next page
-attrib['href']
-follow and follow_all
-Using spider arguments

# BASIC CONCEPTS

## Command line tool

scrapy.cfg inside a Scrapy project’s root
SCRAPY_SETTINGS_MODULE
SCRAPY_PROJECT
SCRAPY_PYTHON_SHELL

### Default project structure

[settings] in scrapy.cfg

### Sharing the root directory

Share [settings]
SCRAPY_PROJECT environment variable to specify a different project for scrapy to use

### Using the scrapy tool

Creating projects
genspider
scrapy -h

```python
Global commands:
    startproject
    genspider
    settings
    runspider
    shell
    fetch
    view
    version

Project-only commands:
    crawl
    check
    list
    edit
    parse
    bench
```

scrapy genspider -**l**

### Custom project commands

-COMMANDS_MODULE
-Register commands via setup.py entry points

## Spiders

-callback function handle response downloaded
-Requests, start_requests(), start_urls, parse
-iterable objects
-parsed data, selector
-saving to database or using Feed **exports**

### scrapy.Spider

-name
-allowed_domains
-start_urls
-[custom_settings](https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref)
-Crawler object vs crawler vs from_crawler() class method
-Settings instance
-logger

```python
    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
```

-state
-start_requests()
-parse
-closed: spider_closed signal.
-Return multiple Requests and items from a single callback

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]

    def parse(self, response):
        for h3 in response.xpath('//h3').getall():
            yield {"title": h3}

        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
```

-use start_requests() directly and give data more structure with Item object

```python
import scrapy
from myproject.items import MyItem

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']

    def start_requests(self):
        yield scrapy.Request('http://www.example.com/1.html', self.parse)
        yield scrapy.Request('http://www.example.com/2.html', self.parse)
        yield scrapy.Request('http://www.example.com/3.html', self.parse)

    def parse(self, response):
        for h3 in response.xpath('//h3').getall():
            yield MyItem(title=h3)

        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)

```

-Spider arguments using __init__ methods or ...:

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'http://www.example.com/categories/{category}']

# or
    def start_requests(self):
        yield scrapy.Request(f'http://www.example.com/categories/{self.category}')
```

-If running Scrapy from a script:

```python
process = CrawlerProcess()
process.crawl(MySpider, category="electronics")

```

if you were to set the **start_urls** attribute from cmd
use ast.literal_eval() or json.loads() and then set it as an attribute

example: set the http auth credentials by HttpAuthMiddleware or UserAgentMiddleware

### **Generic** Spiders

use to subclass your spiders from (parent template)
common scraping cases
    following all links on a site based on certain rules
    crawling from Sitemaps
    parsing an XML/CSV feed

#### CrawlSpider

convenient mechanism for following links by defining a set of **rules**
    rules: Crawling rules
        link_extractor, link_text, meta
        callback, resp, req, meta, ...
        process_links
        process_request
        errback
    parse_start_url

#### XMLFeedSpider

parsing XML feeds by iterating through them by a certain node name
    iterator: {iternodes, xml, and html}
    itertag: name of the **node**
    namespaces
    ...

```python
from scrapy.spiders import XMLFeedSpider
from myproject.items import TestItem

class MySpider(XMLFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']    # xml files
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        '''notice about node'''
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = TestItem()
        item['id'] = node.xpath('@id').get()
        item['name'] = node.xpath('name').get()
        item['description'] = node.xpath('description').get()
        return item
```

#### CSVFeedSpider

very similar to the XMLFeedSpider, except that it iterates over rows, instead of nodes
parse_row() called in each iteration
delimiter | quotechar | headers |

```python
from scrapy.spiders import CSVFeedSpider
from myproject.items import TestItem

class MySpider(CSVFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.csv']    # this csv file
    delimiter = ';'
    quotechar = "'"
    headers = ['id', 'name', 'description'] # cols

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)

        item = TestItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item

```

#### SitemapSpider

crawl a site by discovering the URLs using Sitemaps.

## Selectors

to extract data from the HTML source
XPath or CSS expressions
[XPath](https://devhints.io/xpath) is a language for selecting nodes in XML documents

```python
from scrapy.selector import Selector
from scrapy.http import HtmlResponse    # need example
```

getall() returns a list with all results vs get() always returns a single result

### Nesting selectors

### Selecting element attributes

### select using regular expressions

extract() and extract_first()   : all vs 1st

### Working with XPaths

relative XPaths
Beware of the difference between //node[1] and (//node)[1] ~use many time

#### Using text nodes in a condition

use the text content as argument to an XPath string
.//text() yields a collection of text elements – a node-set when using contains() or starts-with()

```python
sel.xpath("//a[contains(.//text(), 'Next Page')]").getall() # vs
sel.xpath("//a[contains(., 'Next Page')]").getall()
```

A node converted to a string with string(...)

#### Variables in XPath expressions

```python
response.xpath('//div[@id=$val]/a/text()', val='images').get()
```

#### Removing namespaces

when see several namespace declarations including a default
call the Selector.remove_namespaces() method, all nodes can be accessed directly by their names

#### Using [EXSLT](http://acronymsandslang.com/definition/72011/EXSLT-meaning.html) extensions

re operations

```python
from scrapy import Selector
doc = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""
sel = Selector(text=doc, type="html")

sel.xpath('//li//@href').getall()
sel.xpath('//li[re:test(@class, "item-\d$")]//@href').getall()
```

Set operations (eg: set:difference)

```python
from scrapy import Selector
doc = """
<div itemscope itemtype="http://schema.org/Product">
  <span itemprop="name">Kenmore White 17" Microwave</span>
  <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />
  <div itemprop="aggregateRating"
    itemscope itemtype="http://schema.org/AggregateRating">
   Rated <span itemprop="ratingValue">3.5</span>/5
   based on <span itemprop="reviewCount">11</span> customer reviews
  </div>

  <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
    <span itemprop="price">$55.00</span>
    <link itemprop="availability" href="http://schema.org/InStock" />In stock
  </div>

  Product description:
  <span itemprop="description">0.7 cubic feet countertop microwave.
  Has six preset cooking categories and convenience features like
  Add-A-Minute and Child Lock.</span>

  Customer reviews:

  <div itemprop="review" itemscope itemtype="http://schema.org/Review">
    <span itemprop="name">Not a happy camper</span> -
    by <span itemprop="author">Ellie</span>,
    <meta itemprop="datePublished" content="2011-04-01">April 1, 2011
    <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
      <meta itemprop="worstRating" content = "1">
      <span itemprop="ratingValue">1</span>/
      <span itemprop="bestRating">5</span>stars
    </div>
    <span itemprop="description">The lamp burned out and now I have to replace
    it. </span>
  </div>

  <div itemprop="review" itemscope itemtype="http://schema.org/Review">
    <span itemprop="name">Value purchase</span> -
    by <span itemprop="author">Lucas</span>,
    <meta itemprop="datePublished" content="2011-03-25">March 25, 2011
    <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
      <meta itemprop="worstRating" content = "1"/>
      <span itemprop="ratingValue">4</span>/
      <span itemprop="bestRating">5</span>stars
    </div>
    <span itemprop="description">Great microwave for the price. It is small and
    fits in my apartment.</span>
  </div>
  ...
</div>
"""
sel = Selector(text=doc, type="html")
for scope in sel.xpath('//div[@itemscope]'):
    print("current scope:", scope.xpath('@itemtype').getall())
    props = scope.xpath('''
                set:difference(./descendant::*/@itemprop,
                               .//*[@itemscope]/*/@itemprop)''')
    print(f"    properties: {props.getall()}")
    print("")
```

XPath extension function **has-class** | slower in most of the cases

### Built-in Selectors reference

#### Selector objects

#### SelectorList objects

examples on HTML | XML response | node.attrib

## Items (key-value pairs)

extract structured data from unstructured sources

### Types

dictionaries, Item objects, dataclass objects, and attrs objects

#### Working with Item objects

Declaring Item subclasses

Declaring fields

Working with Item objects: Creating, Getting field, Setting field, Accessing, Copying

Extending Item subclasses

## Item Loaders T.B.D

## Scrapy shell T.B.D

## Item Pipeline T.B.D

## Feed exports T.B.D

## Requests and Responses T.B.D

## Link Extractors T.B.D

## Settings T.B.D

## Exceptions T.B.D

# BUILT-IN SERVICES

...
