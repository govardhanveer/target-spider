# -*- coding: utf-8 -*-

"""
    author- Govardhan Veer
    date-   09-05-2021
    What logs to be kept while crawling

"""
import logging
# from scrapy import log #deprecated
from scrapy import logformatter


class PoliteLogFormatter(logformatter.LogFormatter):
    def dropped(self, item, exception, response, spider):
        return {
            'level': logging.DEBUG,
            'format': logformatter.DROPPEDMSG,
            'exception': exception,
            'item': item,
        }

