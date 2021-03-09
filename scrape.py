from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt


# scrapes pairings (ingredientspairing.com)
def pairings_scrape(url_given_ingredient):
    #request website HTML
    ingr_site = 'url_given_ingredient'
    ingr_r = requests.get(ingr_site)


    # read
    with open(ingr_r.text) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    return soup


# scrapes the specifics of item (foodprint.org)
def details_scrape(url_given_ingredient):
    # request website HTML
    ingr_site = 'url_given_ingredient'
    ingr_r = requests.get(ingr_site)


    # read
    with open(ingr_r.text) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    return soup




# parse
def pairings_data():
    '''use ingredientspairing.com'''
    
    return




# parse
def details_data():
    '''use foodprint.org'''

    return