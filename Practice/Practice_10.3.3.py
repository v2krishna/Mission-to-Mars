#!/usr/bin/env python
# coding: utf-8


#10.3.3 
#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# setting the executable path 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Visit the mars nasa news site
url ='http://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)
#OPtional delay for loading the page , searching for div tag with class list_text
browser.is_element_present_by_css('div.list_text', wait_time=1)

html= browser.html
news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

#Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div',class_='content_title').get_text()

news_article_summary  = slide_elem.find('div', class_='article_teaser_body').get_text()

#visit URL 
url ='http://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)

#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


#find the relative image url 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


#adding the base url to our code
# USe the base URL to create and obsolute URL
img_url  = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


#reading the table from the html
df= pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.columns=['description','Mars','Earth']
df.set_index('description',inplace=True)
df


#converting back dataframe to html
df.to_html()
print(df.to_html())

browser.quit() # quit the splinter browser to stop and quit listening to the instructions




