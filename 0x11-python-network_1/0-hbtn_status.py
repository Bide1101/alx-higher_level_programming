#!/usr/bin/python3
"""
This python script fetches a given website using urrlib
"""


import urllib.request

if __name__ == "__main__":
    # The url to fetch is:
    url = 'https://alx-intranet.hbtn.io/status'
    # Sends an HTTP GET request to the URL
    with urllib.request.urlopen(url) as response:
        # This reads the HTML content
        htmlcontent = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(htmlcontent)))
        print("\t- content: {}".format(htmlcontent))
        print("\t- utf8 content: {}".format(htmlcontent.decode('utf-8')))
