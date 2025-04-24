from scrapy.item import Item, Field

class BookingHotelItem(Item):
    id = Field()
    city_id = Field()
    name = Field()
    description = Field()
    url = Field()
    review_appreciation = Field()
    review_score = Field()
    geo_latitude = Field()
    geo_longitude = Field()
    rating_stars = Field()
    rating_squares = Field()
    
