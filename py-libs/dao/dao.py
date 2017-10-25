#!/usr/bin/python
# -*- coding: utf-8 -*-


class dao(object):
    def __init__(self, data):
        self.parsing(data)

    def parsing(self, data):
        # Abstract function
        raise NotImplementedError("parsing function is abstract")

    def trim(self, data):
        data = data.replace(",", "")
        return data

    def trimDate(self, date):
        date = date.replace("/", "")
        return date
