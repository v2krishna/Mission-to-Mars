#!/usr/bin/env python
# coding: utf-8

# In[142]:


#10.3.3 
#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[143]:


# setting the executable path 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#Visit the mars nasa news site
url ='http://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)
#OPtional delay for loading the page , searching for div tag with class list_text
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html= browser.html
news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


#Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div',class_='content_title').get_text()
news_title


# In[7]:


news_article_summary  = slide_elem.find('div', class_='article_teaser_body').get_text()
news_article_summary


# ### Featured Images

# In[8]:


#visit URL 
url ='http://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[9]:


#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


#find the relative image url 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


#adding the base url to our code
# USe the base URL to create and obsolute URL
img_url  = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[13]:


#reading the table from the html
df= pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.columns=['description','Mars','Earth']
df.set_index('description',inplace=True)
df


# In[14]:


#converting back dataframe to html
df.to_html()


# In[15]:





# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[196]:


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)


# In[197]:


hemisphere_image_urls = []   # empty dictionary to hold titles and urls

#get the links of hemispheres
img_link = browser.find_by_css("a.product-item h3")
# find the no of  hemisphere links
no_of_urls =  len(img_link)
print(no_of_urls)
try:
    #loop through the number of urls.
    for i in range(no_of_urls):
        
        # empty dictionary
        hemisphere_dict = {}   
        
        #click on each url using the click()
        browser.find_by_css('a.product-item h3')[i].click() 
        
        #get the title of the hemisphere and add into the dictionary
        hemisphere_dict['title']=  browser.find_by_css('h2.title').text
        
        #just validating the title in the dictionary
        print(hemisphere_dict)
        
        #check links on the Sample text  within the same url 
        img_url_text = browser.links.find_by_text('Sample').first
        
        #add to the hemisphere dict 
        hemisphere_dict['img_url'] = img_url_text['href']
        print(hemisphere_dict)
        
        #append the to empty list
        hemisphere_image_urls.append(hemisphere_dict)

        browser.back()
except :
    print('Not in a vald link')


# In[198]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


browser.quit() # quit the splinter browser to stop and quit listening to the instructions

