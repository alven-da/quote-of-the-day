class CreateOrUpdateQuoteDTO:
  def __init__(self, author: str, quote: str):
    self.author = author
    self.quote = quote

class QuoteOutputDTO:
  def __init__(self, id: str, author: str, quote: str):
    self.id = id
    self.author = author
    self.quote = quote