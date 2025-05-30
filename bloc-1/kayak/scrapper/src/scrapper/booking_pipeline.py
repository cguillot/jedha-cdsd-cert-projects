from itemadapter import ItemAdapter
from booking_items import BookingHotelItem

class BookingHotelScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if isinstance(item, BookingHotelItem):
            adapter['id'] = int(adapter['id'])
            adapter['city_id'] = int(adapter['city_id'])

            if adapter['review_score']:
                adapter['review_score'] = adapter['review_score'].replace(',','.')

            adapter['review_appreciation'] = self.clean_description_str(adapter['review_appreciation'])

            adapter['description'] = self.clean_description_str(adapter['description'])

            if not adapter.get('rating_stars'):
                adapter['rating_stars'] = 0

            if not adapter.get('rating_squares'):
                adapter['rating_squares'] = 0

            spider.logger.info(f"Processed hotel item {item['name']} ({item['url']})")

        return item

    @staticmethod
    def clean_description_str(descritpion: str):
        if descritpion:
            # remove some special characters:
            # - \xa0: unbreakable space
            return descritpion.replace('\xa0', ' ').replace("\u2019","'").strip()
