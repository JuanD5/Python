from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent 
        
    @property    
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string
    
    @property    
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string
    
    @property    
    def tags(self):
        locator = QuoteLocators.TAGS
        return self.parent.select(locator).string
    
    def __repr__(self) -> str:
        return f'Quote {self.content} by {self.author}'