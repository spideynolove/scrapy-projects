
# Saving deal with new domains and start_urls

```python
# -*- coding: utf-8 -*-
import scrapy
 
 
class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
 
    start_urls = [
        'https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html'
    ]
 
    def parse(self, response):
        pass
```

# [stackoverflow](https://stackoverflow.com/questions/43960422/feed-export-encoding-option-not-working-for-for-items-files-in-scrapyd-python)

# [glassesshop_exercise](https://www.glassesshop.com/bestsellers)
