from scrapy import Item, Field


class FixtureItem(Item):
    week = Field()
    season = Field()
    host = Field()
    guest = Field()
    stadium = Field()
    attendance = Field()

class ClubItem(Item):
    team = Field()
    ground = Field()
    # overall = Field()
    # home = Field()
    # away = Field()
    # form = Field()