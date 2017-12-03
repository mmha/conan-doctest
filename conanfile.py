#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class DoctestConan(ConanFile):
    name = "doctest"
    version = "1.2.6"
    generators = "cmake"
    url = "https://github.com/mmha/conan-doctest"
    license = "https://github.com/onqtam/doctest/blob/1.2.6/LICENSE.txt"
    description = "The fastest feature-rich C++98/C++11 single-header testing framework for unit tests and TDD"

    def source(self):
        header_name = "doctest.h"
        tools.download("https://raw.githubusercontent.com/onqtam/doctest/%s/doctest/%s" % (self.version, header_name), header_name)
        
    def package(self):
        self.copy(pattern="doctest.h", dst="include")

    def package_id(self):
        self.info.header_only()
