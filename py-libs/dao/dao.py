#!/usr/bin/python
# -*- coding: utf-8 -*-


class dao(object):
    def __init__(self, data):
        self.parsing(data)

    def parsing(self, data):
        # Abstract function
        raise NotImplementedError("parsing function is abstract")