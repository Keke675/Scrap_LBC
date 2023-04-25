from bs4 import BeautifulSoup
import requests
import os
import codecs

def get_data(url_given):
    f = codecs.open("C:/Users/Kevin/Documents/Repos/Recherche_LBC/Scraping/downloads/" + url_given + ".html", "r", 'utf-8')

    doc = BeautifulSoup(f, "html.parser")

    data = {
        "price": doc.find("div", {"data-qa-id": "adview_price", "display": "flex"}).find("span").text.replace(u'\xa0', u' ') ,
        "adress" : doc.find("a", {"href" : "#map"}).text.replace(u'\xa0', u' ') ,
        "surface" : doc.find("div", {"data-qa-id": "criteria_item_square"}).find("div").find("span").text.replace(u'\xa0', u' ') ,
        "rooms" : doc.find("div", {"data-qa-id": "criteria_item_rooms"}).find("div").find("span").text.replace(u'\xa0', u' ') ,
        "url" : doc.find("link", {"rel": "canonical"})["href"] ,
    }
    print(data)
    return data

    

