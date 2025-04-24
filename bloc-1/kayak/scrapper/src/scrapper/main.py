import argparse
from booking_spider import SingleDestinationHotelsBookingSpider
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import CsvItemExporter
import scrapy.utils.log
from colorlog import ColoredFormatter
import logging
import copy
import twisted

parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--city-id', type=str, required=True)
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--latitude', type=str, required=True)
parser.add_argument('--longitude', type=str, required=True)
parser.add_argument('--json-store-file-path', type=str, required=True)

# Parse the argument
args = parser.parse_args()

print(f"Scrapping hotels for destination: {args.name} (id: {args.city_id}, latitude: {args.latitude}, longitude: {args.longitude})")

class HeadlessCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        # args[0] is (opened) file handler
        # if file is not empty then skip headers
        args[0].seek(0,2)
        if args[0].tell() > 0:
            kwargs['include_headers_line'] = False

        super(HeadlessCsvItemExporter, self).__init__(*args, **kwargs)

# setup colored logs
color_formatter = ColoredFormatter(
    (
        '%(log_color)s%(levelname)-5s%(reset)s '
        '%(yellow)s[%(asctime)s]%(reset)s'
        '%(white)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)d%(reset)s '
        '%(log_color)s%(message)s%(reset)s'
    ),
    datefmt='%y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'blue',
        'INFO': 'bold_cyan',
        'WARNING': 'red',
        'ERROR': 'bg_bold_red',
        'CRITICAL': 'red,bg_white',
    }
)

_scrapy_logs_get_handler = copy.copy(scrapy.utils.log._get_handler)

def _scrapy_logs_get_handler_custom(*args, **kwargs):
    handler = _scrapy_logs_get_handler(*args, **kwargs)
    handler.setFormatter(color_formatter)
    return handler

scrapy.utils.log._get_handler = _scrapy_logs_get_handler_custom

settings = {
    'ITEM_PIPELINES': {
        'booking_pipeline.BookingHotelScraperPipeline': 1
    },
    'FEEDS': {
        f"{args.json_store_file_path}": {"format": "jsonlines", 'overwrite': False},
    },
    'FEED_EXPORTERS': {
        'csv': 'main.HeadlessCsvItemExporter',
    },
    'OVERWRITE': True,
    'LOG_LEVEL': logging.DEBUG,
    'LOG_STDOUT': True,
    'AUTOTHROTTLE_ENABLED': True,
    'HTTPCACHE_ENABLED': True,
    'TELNETCONSOLE_ENABLED': False,
    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    # Set settings whose default value is deprecated to a future-proof value
    # 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
    'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
    'FEED_EXPORT_ENCODING': 'utf-8',
}


process = CrawlerProcess(settings)
process.crawl(SingleDestinationHotelsBookingSpider, city_id=args.city_id, city=args.name, latitude=args.latitude, longitude=args.longitude, max_hotels_to_search=20)

try:
    process.start()
except twisted.internet.error.ReactorNotRestartable:
    # Hide ReactorNotRestartable error from jupyter notebook execution
    pass
