import requests
from pages.quotes_pages import QuotesPage

page_content = requests.get("http://quotes.toscrape.com").content
page = QuotesPage(page_content)

if __name__ == "__main__":  
    for quote in page.quotes:
        print(quote)


    