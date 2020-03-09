import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import time
import pandas as pd


mars_web = {}

# Initialize browser
def init_browser():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# Latest News Headline and Body Scraping
def scrape_news():

    Browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    Browser.visit(url)
    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')
    headline = soup.find('div', class_='content_title').find('a').text
    body = soup.find('div', class_='rollover_description_inner').text

    mars_web['headline'] = headline
    mars_web['body'] = body

    return mars_web

# Featured Image Scraping
def scrape_img():

    Browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    Browser.visit(url)
    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find('footer').find('a')['data-fancybox-href']
    featured_image_url = f'https://www.jpl.nasa.gov{image_url}'
   
    mars_web['featured_image_url'] = featured_image_url

    Browser.quit()
    return mars_web

# Twitter Weather Scraping
    # url = 'https://twitter.com/marswxreport?lang=en'
    # browser.visit(url)
    # time.sleep(1)

    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # weather_tweet = soup.find()
    # weather_tweet

# Mars Facts Scraping
def mars_facts_scrape():

    Browser = init_browser()
    url = 'https://space-facts.com/mars/'
    Browser.visit(url)
    mars_df = pd.read_html(url)[2]
    mars_df.columns = ['Description', 'Value']
    mars_df

    mars_df_html = mars_df.to_html()

    mars_web['mars_df_html'] = mars_df_html

    Browser.quit()
    return mars_web


# Hemisphere Images Scraping
def hemishpere_scrape():

    Browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Browser.visit(url)
    time.sleep(1)

    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    for item in items:
    
        hem_dict = {}
    
        title = item.find('h3').text
        hem_dict['title'] = title
    
        tag = item.find('a')['href']
        img_url = url + tag
        Browser.visit(img_url)
    
        hem_dict['img_url'] = img_url
        hemisphere_image_urls.append(hem_dict)
    
    Browser.quit()
    return mars_web


