
import requests
from bs4 import BeautifulSoup
import streamlit as st
import pickle
import spacy




# specify the URL of the news website to scrape
url = "https://www.theverge.com/"

# send a GET request to the website URL and store the response
response = requests.get(url)

# parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the news article links on the website
article_links = soup.find_all("a", class_="group-hover:shadow-underline-franklin")

l = []
links = []

# loop through each article link and scrape the article text
for link in article_links:
    # extract the URL of the article
    article_url = link["href"]
    
    # send a GET request to the article URL and store the response
    article_response = requests.get(url + article_url)
    links.append(url + article_url)

#     # parse the HTML content of the article using BeautifulSoup
    article_soup = BeautifulSoup(article_response.content, "html.parser")
    
#     # find the main text content of the article and print it
    article_text = article_soup.find("div", class_="clearfix").get_text()
    l.append(article_text)

nlp = pickle.load(open("save.p", "rb"))


summaries = []
percentages = []


st.title("Daily Tech stories summarizer")
text = " Read full article here"

for i in l:
	st.write(i)