from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from imdb.spiders.bestmovies import BestmoviesSpider


process = CrawlerProcess(settings=get_project_settings())
process.crawl(BestmoviesSpider)
process.start()