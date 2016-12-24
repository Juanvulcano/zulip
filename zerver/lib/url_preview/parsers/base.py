from __future__ import absolute_import
from typing import Any
from six import Text
from bs4 import BeautifulSoup


class BaseParser(object):
    def __init__(self, html_source):
        # type: (Text) -> None
        self._soup = BeautifulSoup(html_source, "lxml")

    def extract_data(self):
        # type: () -> Any
        raise NotImplemented
