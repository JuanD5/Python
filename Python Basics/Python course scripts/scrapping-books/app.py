import requests
from pages.book_pages import AllBooksPage


page_content = requests.get("http://books.toscrape.com").content
page = AllBooksPage(page_content)

books = page.books 

if __name__ == "__main__":  
    for book in books:
        print(book)
        
    