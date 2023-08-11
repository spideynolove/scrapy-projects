BOT_NAME = "crawldata"

SPIDER_MODULES = ["crawldata.spiders"]
NEWSPIDER_MODULE = "crawldata.spiders"

# ROTATING_PROXY_LIST_PATH = '/home/proxies.txt'
# ROTATING_PROXY_PAGE_RETRY_TIMES=100

URLLENGTH_LIMIT = 50000
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOW_ALL = True
# CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 1
# RANDOMIZE_DOWNLOAD_DELAY = True
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 1
TELNETCONSOLE_ENABLED = False

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