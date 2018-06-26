﻿﻿
 # Bing Scraper

The bingscraper is python3 package which extracts the text and images content on search engine `bing.com`.

It helps the user in a way that he/she will be getting only meaningful results and images for their search query. It does not download the ad content and hence saving data for the user.

The script working in background requests for a search term and creates directory (if not made previously) in the root directory of the script where all the content of the related particular search is stored. This script will be downloading the hypertext and hyperlink to that text and saving it to a .txt file within the directory made by itself. This directory saves the text content as well as the images downloaded using the script.

## Requirements
1.	Modules:

    a. `requests`: For requesting content through two HTTPS Methods: `GET` and `POST`. Used `GET` Method.
        
    b. `BeautifulSoup`: For creating JSON like dictionary using HTML Parser. Package uses `bs4`.
    
    c. `os`: For checking and making directories.
    
    d. `PIL.Image`: `Pillow Module`. For extracting image content.
    
    e. `io.ByteIO`: For saving the extracted image using the `PIL.Image`.

2.	Internet Connection: Continuous high speed internet connection is required for the proper function of the python package as  it continuously creates the copy of the images into the local machine.

3.  Python: Version 3.5.6 or above. This package is written in `python 3.5.6`

## Installation

For python installation:

`pip install bingscraper`
or 
`python -m pip install bingscraper`

For Anaconda installation:

`conda install bingscraper`

## How to use

Install the above modules. Successful import of `bingscraper` depends only after the above imports.

Sample code in python:

`import bingscraper as bs`

`search = str(input())`

`bs.scrape(search)`

Function scrape() takes an string argument and does the scraping work.