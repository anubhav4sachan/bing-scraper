# -*- coding: utf-8 -*-
import os
import requests as re
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

class scrape:
    def __init__(self, term):
        self.search_term = term
        self.dir_name = self.search_term.replace(" ", "_").lower()
        if not os.path.isdir(self.dir_name):
            os.makedirs(self.dir_name)
    def getSearch(self):
        return self.search_term
    def getDir(self):
        return self.dir_name
    
    def text(self): 
        param = {"q": self.getSearch()}
        try:
            rt = re.get("https://www.bing.com/search", params = param)
            soupt = BeautifulSoup(rt.text, "html.parser")
        except:
            print("Internet Disconnected. Connect to download text.")
    
        results = soupt.find("ol", {"id":"b_results"})
        lists = results.findAll("li", {"class":"b_algo"})
        file = open("./"+ self.getDir() + "/" + self.getSearch() +".txt", 'w')
        file.close()
        for item in lists:
            item_text = item.find("a").text
            item_href = item.find("a").attrs["href"]
            if item_text and item_href:
                print(item_text + "\n" + item_href + "\n")
                file = open("./"+ self.getDir() + "/" + self.getSearch() +".txt", 'a')
                file.write(item_text + "\n" + item_href + "\n\n")
                file.close()
    
    def image(self):
        param = {"q": self.getSearch()}
        try:
            ri = re.get("https://www.bing.com/images/search", params = param)
            soupi = BeautifulSoup(ri.text, "html.parser")
            links = soupi.findAll("a", {"class":"thumb"})
            for item in links:
                try:
                    img_obj = re.get(item.attrs["href"])
                    print("Downloading: ", item.attrs["href"])
                    title = item["href"].split("/")[-1]
                    try:
                        img = Image.open(BytesIO(img_obj.content))
                        img.save("./"+ self.getDir() + "/" + title, img.format)
                    except:
                        print("Could not Save :\'(")
                except:
                    print("Image cannot be requested.")
        except:
            print("Internet Disconnected. Connect to download images.")