from crawldata.functions import random_user_agent

BOT_NAME = 'crawldata'
SPIDER_MODULES = ['crawldata.spiders', 'crawldata.spiders.market']
NEWSPIDER_MODULE = 'crawldata.spiders'
USER_AGENT = random_user_agent()

URLLENGTH_LIMIT = 50000
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOW_ALL = True
DOWNLOAD_DELAY = 1
TELNETCONSOLE_ENABLED = False

#CONCURRENT_REQUESTS = 32
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# # pip install scrapy-rotating-proxies
# ROTATING_PROXY_LIST_PATH = '/home/proxies.txt'
# ROTATING_PROXY_PAGE_RETRY_TIMES=100

# # Un lock this block if use proxies
# DOWNLOADER_MIDDLEWARES = {
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }

# ITEM_PIPELINES = {
#     'crawldata.pipelines.CrawldataPipeline': 300,
# }

LOG_ENABLED = True
LOG_LEVEL = 'ERROR'
LOG_FORMAT = '%(levelname)s: %(message)s'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'