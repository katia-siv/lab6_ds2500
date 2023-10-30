#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:29:35 2023

@author: ekaterinasivokon
"""
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# =============================================================================
# Problem 1 (Scrape)
# =============================================================================

def construct_links(url):
    '''Write a function that, given a URL, returns a list of tuples (x, y) where
        x is a link and y is a label for that link.
        For example, if the web page contains the tag <a href="page1.html">click
        here!</a>, then your list would contain the tuple ("page1.html", "click
        here!")
        Here are the specs:
        Function name: construct_links
        Parameters: URL (string)
        Returns: list of tuples (strings)
    '''
    # HTTP request to URL
    response = requests.get(url)
    # Parse
    parse_attr = BeautifulSoup(response.content, "html.parser")
    # Find all <a> tags
    ssylka = parse_attr.find_all("a")
    tup_list = [(link.get("href"), link.text) for link in ssylka]
    return tup_list

# =============================================================================
# Problem 2 (More Scraping)
# =============================================================================

def count_missing_alt(url):
    '''Write a function that, given a URL, computes and returns the percent of
       images that do not have an alt attribute. Anytime “alt” is missing from
       an image, it has a negative impact on web users with visual impairments,
       so it can be helpful to draw attention to it for web developers and
       reviewers. For example, if the web page contains the following image tags:
         <img src = "img.jpg" alt = "My Image">
        <img src = "img.jpg">
        <img src = "img.jpg" alt = "">
        ... then your function would return .66667.
        Here are the specs:
        Function name: count_missing_alt
        Parameters:  URL (string)
        Returns: a float, the percent of image tags without an alt attribute.
        If there are no images on the page at all, your function should return 0.
    '''
    # HTTP request to URL
    response = requests.get(url)
    # Parse 
    parse_attr = BeautifulSoup(response.content, "html.parser")
    # Find all <img> tags
    images = parse_attr.find_all("img")
    # Count # of images without alt
    no_alt = sum(1 for img in images if not img.has_attr("alt"))

    length = len(images)
    if length == 0:
        return 0.0
    else:
        return float(no_alt) / length
    
# =============================================================================
# Problem 3 (NLP)
# =============================================================================

def paragraph_polarity(url, div_class):
    '''Write a function that, given a URL to a Reddit post and a div tag (string),
        computes and returns the polarity score of the post text (ignore the post
        title,  comments, and other content on the page).
        Here are the specs:
        Function name: paragraph_polarity
        Parameters:  URL (string) of a reddit page, and div class (string)
        Example URL: "https://www.reddit.com/r/NEU/comments/15q56w7/transferring_to_neu_computer_science_without/"
        Reddit’s key div class: "mb-sm  mb-xs px-md xs:px-0"
        Returns: a float, the polarity score of the post text
    '''
    # HTTP request to URL
    response = requests.get(url)
    # Parse 
    parse_attr = BeautifulSoup(response.content, "html.parser") 
    # Find <div> tag 
    div = parse_attr.find("div", {"class": div_class})
    # Find 1st <p> tag
    paragraph = div.find("p")
    # Polarity score
    score = TextBlob(paragraph.text).sentiment.polarity
    return float(score)

# =============================================================================
# Problem 4 (Calling API Functions)
# =============================================================================

api_key = "17be473d45fb41066a5f897fae8dccf0"

# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

def get_weather_json(lat, lon, api_key):
# API URL with the given latitude, longitude, and API key    
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&appid={api_key}"
# API call to the One Call API 3.0
    response = requests.get(url)
# Parse the JSON response
    data = response.json()
# Extract weather data from JSON response
    current = data["current"]
    dict_weather = {
        "temperature": current["temp"],
        "feels_like": current["feels_like"],
        "humidity": current["humidity"],
        "pressure": current["pressure"],
        "wind_speed": current["wind_speed"],
        "wind_direction": current["wind_deg"],
        "description": current["weather"][0]["description"],
        "icon": current["weather"][0]["icon"]
    }

    return dict_weather