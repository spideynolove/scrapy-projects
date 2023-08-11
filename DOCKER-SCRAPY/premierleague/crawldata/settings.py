from crawldata.functions import random_user_agent

BOT_NAME = 'crawldata'
SPIDER_MODULES = ['crawldata.spiders']
NEWSPIDER_MODULE = 'crawldata.spiders'
USER_AGENT = random_user_agent()

# pip install scrapy-rotating-proxies
# ROTATING_PROXY_LIST_PATH = '/home/proxies.txt'
# ROTATING_PROXY_PAGE_RETRY_TIMES=100

URLLENGTH_LIMIT = 50000
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOW_ALL=True
# CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 0.1
RANDOMIZE_DOWNLOAD_DELAY = True
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 1
TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.premierleague.com',
    'Referer': 'https://www.premierleague.com/',
}

# # Un lock this block if use proxies
# DOWNLOADER_MIDDLEWARES = {
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }

# ITEM_PIPELINES = {
#     'crawldata.pipelines.CrawldataPipeline': 300,
# }

LOG_ENABLED = True
LOG_LEVEL='ERROR'
LOG_FORMAT = '%(levelname)s: %(message)s'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

# Redis Connection URL
# REDIS_URL = 'redis://default:JWn5sxbhFWFnA8mqNsVohXjWMOQFOQ0D@redis-10186.c265.us-east-1-2.ec2.cloud.redislabs.com:10186'
REDIS_URL = 'redis://127.0.0.1:6379'

# MONGODB_URI = "mongodb://127.0.0.1:27017"
MONGODB_URI = "mongodb://192.168.0.102:27017"
MONGODB_DATABASE = "premierleague"