# Common problems

## Commons data vs individual data

- common data ~ co + xxx file
- individual ~ in + xxx file

## SCRIPTS

- Big picture
+ Calendars
+ News
+ Positions

- detail quotes
+ Market

## 30052023 

- Positions/ Position Stats (detail of the first)
    + Trader, percent, lot
    + entry
    + win/ lose ...

- Long-Short Ratio

## DATA MODELS

- idea
    + split news to individual topic to get more content from each news
    examples:
        https://www.forexfactory.com/news/1224002-ecbs-vujcic-inflation-risks-are-still-tilted-to

## Checklist parameterization

### indicators_news
    ---------------------------------------------
    ['eurusd', 'audusd', 'nzdusd', 'usdjpy', 'usdchf', 'usdcad', 'gbpusd', 
    'euraud', 'eurnzd', 'eurcad', 'eurchf', 'eurjpy', 'eurgbp', 
    'gbpaud', 'gbpnzd', 'gbpcad', 'gbpchf', 'gbpjpy', 
    'xauusd', 'xagusd', 
    'audnzd', 'audcad', 'audchf', 'audjpy', 
    'nzdcad', 'nzdchf', 'nzdjpy', 
    'cadchf', 'cadjpy', 
    'chfjpy']
    ---------------------------------------------
    INTERVALS = ('M5', 'H1', 'H4', 'D1', 'MN1')

### instruments

    ---------------------------------------------
    ['eurusd', 'audusd', 'nzdusd', 'usdjpy', 'usdchf', 'usdcad', 'gbpusd', 
    'euraud', 'eurnzd', 'eurcad', 'eurchf', 'eurjpy', 'eurgbp', 
    'gbpaud', 'gbpnzd', 'gbpcad', 'gbpchf', 'gbpjpy', 
    'audnzd', 'audcad', 'audchf', 'audjpy', 
    'nzdcad', 'nzdchf', 'nzdjpy', 
    'cadchf', 'cadjpy', 
    'chfjpy']
    ---------------------------------------------
    SPX/USD, FTSE100/USD, DXY/USD, WTI/USD, VIX/USD,
    Nikkei225/USD, Gold/USD
    ---------------------------------------------

### bars

    ---------------------------------------------
    ['eurusd', 'audusd', 'nzdusd', 'usdjpy', 'usdchf', 'usdcad', 'gbpusd', 
    'euraud', 'eurnzd', 'eurcad', 'eurchf', 'eurjpy', 'eurgbp', 
    'gbpaud', 'gbpnzd', 'gbpcad', 'gbpchf', 'gbpjpy', 
    'audnzd', 'audcad', 'audchf', 'audjpy', 
    'nzdcad', 'nzdchf', 'nzdjpy', 
    'cadchf', 'cadjpy', 
    'chfjpy']
    ---------------------------------------------
    SPX/USD, FTSE100/USD, DXY/USD, WTI/USD, VIX/USD,
    Nikkei225/USD, Gold/USD
    ---------------------------------------------
    INTERVALS = ('M5', 'M15', 'M30', 'H1', 'H4', 'D1', 'W1', 'MN1')
    ---------------------------------------------
    per_page = x, ... 9999

### news

    news type: lastest | hottest | most12h | lastFA | lastTA    ~ 1st version
    quote name                                                  ~ 2nd version
    - can't get detail post because js
        install headless version of chrome or firefox

### positions

    INTERVALS = 'M5', 'H1', 'D1'
