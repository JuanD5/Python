from locators.books_locators import BookLocators
import re


class BookParser:
    
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    def __init__(self, parent) -> None:
        self.parent = parent
    
    @property    
    def name(self):
        locator = BookLocators.NAME  # CSS locator
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs.get('title')
        return item_name
    
    @property      
    def price(self):
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))
    
    @property  
    def rating(self):
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [tag_class for tag_class in classes if tag_class != 'star-rating']
        rating_number = self.RATINGS[rating_classes[0]]
        return rating_number
    
    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.price} and {self.rating} stars>'