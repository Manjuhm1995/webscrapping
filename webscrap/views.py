import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import csv

def scrape_news(request):
    # Make a request to the website
    url = 'http://quotes.toscrape.com/'  # Replace with the actual website URL
    response = requests.get(url)
    # print(response.content)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes=soup.find_all('span',attrs={'class':'text'})
    authors=soup.find_all('small',attrs={'class':'author'})
    # file = open('scraped-data.csv', 'w')
    # writer = csv.writer(file)
    # writer.writerow(["quotes", "authors"])
    dis_authors=[]
    dis_quotes=[]
    for quote,author in zip(quotes,authors):
        print(quote.text+"  -  "+author.text)
        dis_quotes.append(quote.text)
        dis_authors.append(author.text)
    #     writer.writerow([quote.text, author.text])
    # file.close()

    # for author in authors:
    #     print(author.text)
    # print(soup)

    # Scrape the news article titles
    # news_titles = []
    # articles = soup.find_all('article')  # Adjust the HTML structure according to the target website
    # print(articles)
    # for article in articles:
    #     title = article.find('h1').text.strip()
    #     news_titles.append(title)

    # Render the scraped data in a template
    # print(news_titles)
    context={'authors':dis_authors,'quotes':dis_quotes}
    return render(request, 'webscrap/base.html', context)
