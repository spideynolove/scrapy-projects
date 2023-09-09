# Work time and schedule

## parameterization

## How design database

## Insight
    Market contains:
        News:
            try new design (based on multiple start_requests)       OK
        upcoming                                                    OK
        
        bars
            /                                                       OK
            /aggregate
                fx                                                  same as base bars
                VIX, Dxy, ...                                       same as base bars
        indicators
            /news                                                   OK
            /breakers                                               SHIT
        instruments                                                 
            fx                                                      OK
            VIX, Dxy, ...                                           OK
        positions                                                   OK
            ??? need split to a single file

    Calendar Events (Total)                                         OK

## Insight other sites

    energyexch : https://www.energyexch.com/
        instruments=WTI/USD,Brent/USD,NatGas/USD,HeatOil/USD,Gasoline/USD,Brent/WTI,WTI/Gasoline,Gold/WTI

    metalsmine
        https://www.metalsmine.com/
        instruments=Gold/USD,Silver/USD,Platinum/USD,Palladium/USD,Copper/USD,Dow/Gold,BTC/Gold,Gold/Silver

    cryptocraft
        https://www.cryptocraft.com/
        instruments=BTC/USD,ETH/USD,DOGE/USD,LTC/USD,BCH/USD,XMR/USD,ETC/USD,BSV/USD