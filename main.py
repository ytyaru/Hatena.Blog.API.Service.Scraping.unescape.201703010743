#!python3
#encoding:utf-8
import xmltodict
from collections import OrderedDict
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
import datetime
import xml.sax.saxutils
import html

class Scraping(object):
    def __init__(self):
        pass

    def scrape(self):
        soup = BeautifulSoup(self.__load_file("../resource/201702281505/ytyaru.ytyaru.hatenablog.com.Services.xml"), 'lxml')
        blog = self.__parse_to_blog_info(soup)
        entries = self.__parse_to_entries_info(soup)
        
    def __load_file(self, file_name, encoding='utf-8'):
        with open(file_name, mode='r', encoding=encoding) as f:
            return f.read()

    def __parse_to_blog_info(self, soup):
        blog_info = {}
        blog_info['title'] = soup.find('title').string
        blog_info['next'] = soup.find('link', rel='next').get('href')
        print(blog_info['title'])
        print(blog_info['next'])
        return blog_info
        
    def __parse_to_entries_info(self, soup):
        entries_info = []
        for entry in soup.find_all('entry'):
            e = {}
            e['title'] = entry.find('title').string
            print(e['title'])
            print(html.unescape(entry.find('content').string))
            entries_info.append(e)
        return entries_info


if __name__ == '__main__':
    client = Scraping()
    client.scrape()

