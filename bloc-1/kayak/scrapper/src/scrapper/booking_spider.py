import scrapy
from booking_items import BookingHotelItem


class SingleDestinationHotelsBookingSpider(scrapy.Spider):
    name = "booking_com_hotels"

    INDEX_URL = "https://www.booking.com/index.fr.html"

    BASE_SEARCH_URL = "https://www.booking.com/searchresults.fr.html"

    # Let start from Booking FR index
    start_urls = [
        INDEX_URL,
    ]

    max_hotels_to_search = 2

    def parse(self, response):
        city = getattr(self, 'city', None)  # self.city
        postal_code = getattr(self, 'postal_code', None)  # self.postal_code
        country = getattr(self, 'country', None)  # self.country

        if city is None:
            self.logger.error("city must be provided")
            return

        search = city
        if postal_code is not None:
            search = f"{search}, {postal_code}"
        if country is not None:
            search = f"{search}, {country}"

        latitude = self.latitude
        longitude = self.longitude

        # Note:
        # - latitude and longitude are not used by web site, but, it works. Thus, I use latitude and longitude to get the search results.
        # - the name isn't mandatory if using lat/lon!
        data = {
            # 'ss': search,
            'lang': 'fr',
            'latitude': latitude,
            'longitude': longitude,
            # filter scores at least 8.0
            'nflt': 'review_score=90;review_score=80',
        }

        self.logger.info(f"Scrapping hotels for city: {data}")

        # Submit search form with location and parse results using parse_search_results
        return scrapy.FormRequest.from_response(
            response,
            formdata=data,
            callback=self.parse_search_results
        )

    def parse_search_results(self, response):
        self.logger.info('parse_search_results')

        # Search all anchors (urls) of returned hotels
        hotel_a_elems_xpath = '//*[@data-results-container="1"]//a[@data-testid="title-link"]'

        max_search = 2

        if self.max_hotels_to_search is not None:
            max_search = self.max_hotels_to_search

        count = 0
        hotels = response.xpath(hotel_a_elems_xpath)

        self.logger.info(
            f"Found {len(hotels)} hotels. Scrapping first {max_search} hotels")

        for hotel in hotels:
            # scrape single hotel informations
            hotel_url = hotel.attrib["href"]
            if hotel_url:
                yield scrapy.Request(hotel_url, callback=self.parse_hotel_info)
            else:
                self.logger.warning("No URL found in {hotel}")

            count += 1
            if count >= max_search:
                break

    def parse_hotel_info(self, response):
        """
        Parse hotel info from the given link
            * id
            * name
            * Url to its booking.com page
            * description
            * Its coordinates: latitude and longitude
            * Score given by the website users
            * Text description of the hotel
        """
        self.logger.info('Parsing hotel info')

        hotel = BookingHotelItem()

        # id
        hotel['id'] = response.xpath('//input[@name="hotel_id"]/@value').get()
        hotel['city_id'] = getattr(self, 'city_id', None)

        hotel['name'] = response.xpath(
            '//*[@id="hp_hotel_name"]//h2/text()').get()

        # Scoring: user friendly appreciation, user score
        hotel['review_appreciation'] = response.xpath(
            '//div[@data-testid="review-score-right-component"]/div[2]/*/text()').get()
        hotel['review_score'] = response.xpath(
            '//div[@data-testid="review-score-right-component"]/div[1]/text()').get()

        # rating: stars or squares
        # stars
        rating_stars_span = response.xpath(
            '//span[@data-testid="rating-stars"]/span')
        if rating_stars_span:
            hotel['rating_stars'] = len(rating_stars_span.getall())

        # squares
        rating_squares_span = response.xpath(
            '//span[@data-testid="rating-squares"]/span')
        if rating_squares_span:
            hotel['rating_squares'] = len(rating_squares_span.getall())

        # Description
        hotel['description'] = response.xpath(
            '//*[@data-testid="property-description"]/text()').get()

        # Geo location
        # OLD: lat_long_str = response.xpath('//*[@id="hotel_header"]').attrib['data-atlas-latlng']
        lat_long_str = response.xpath(
            '//*[@id="map_trigger_header"]').attrib['data-atlas-latlng']
        lat_long = lat_long_str.split(',')
        hotel['geo_latitude'] = lat_long[0]
        hotel['geo_longitude'] = lat_long[1]

        # Direct url to the hotel on Booking.com
        hotel['url'] = response.xpath(
            '/html/head/link[@rel="canonical"]').attrib['href']

        yield hotel
