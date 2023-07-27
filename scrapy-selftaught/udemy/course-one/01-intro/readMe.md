
# Web scraping

## Data extract

- text
- images
- videos
- emails
  
## Scrapy

- suitable for complex projects
  
## Other: requests, bs4

## Scrapy components

- Spiders: **what we want scrape**
  
+scrapy>spider
+crawlspider

+xmlFeed
+csvFeed
+sitemap
  
- pipelines: **extract data process**
  
+clean
+remove dup
+store

- middlewares: **relate rq & reps**
  
+Request/Response
+inject custom headers
+use proxies

- engine: **ensure the operations consistency**

- scheduler: **operations order**
+queue
+FIFO

## Web root dir: robots.txt -> check this

- user-agent: identity
- allow: pages that spider allowed
- disallow: forbidden pages

## Installation

- Anaconda
- VS code
  