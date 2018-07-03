# -*- coding: utf-8 -*-

import setuptools

try:
    README_DESC = open('README_DESC.md').read()
except:
    README_DESC = '"README_DESC.md" not found'

VERSION = '2.0'
NAME = 'bingscraper'
SHORT_DESC = 'The BingScraper is python3 package having function to extract the text and images content on search engine `bing.com`.'
AUTHOR = 'Anubhav Sachan'
EMAIL = 'anubhav4sachan@gmail.com'
LICENSE = 'GNU GPL v3'
URL = 'https://www.github.com/anubhav4sachan/bing-scraper'
PKG = ['bingscraper']

setuptools.setup(
        name = NAME,
        version = VERSION,
        description = SHORT_DESC,
        long_description = README_DESC,
        url = URL,
        author = AUTHOR,
        author_email = EMAIL,
        packages = PKG
)