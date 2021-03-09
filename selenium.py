"""
This program will go through site and input the given key word from voice recognition
and submit it to find the url. The url will be passed to the scrape.py module where it will
scrape the page of the given key word/s.

---------------- Psuedocode -----------

This is for a single item/word:
    - import selenium
    - identify search bar
    - input key word
    - click submit

This is for detail of item (foodprint.org):
    - import selenium
    - search site https://foodprint.org/?s=
    - identify search bar
    - click submit
    - compare key word with link names (needs to be exact ==)


"""

