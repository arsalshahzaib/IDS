from pydoc import source_synopsis
from urllib import response
import requests
from bs4 import BeautifulSoup

page    =   requests.get("https://hltv.org")
soup    =   BeautifulSoup(page.content, "html.parser")

response    =   soup.find_all('div', {"class": "newstext"})     #   finds the div tag with the class name of 'newstext'
# text    =   response


print(response)