import logging

from quote_of_the_day.core.entities import Quote
# from quote_of_the_day.repository.quote_repository import QuoteRepository
from quote_of_the_day.repository.quote_mock_repository import QuoteMockRepository

class QuoteService():
  def get_quote_by_id(id: str):
    quote = QuoteMockRepository.get_quote_by_id('1234')
    return quote
  
  def create_quote(quote):
    for_save = Quote(id='', author=quote.get('author'), quote=quote.get('quote'), date='')
    entity = QuoteMockRepository.create_quote(for_save)

    return {
      "id": entity.id,
      "author": entity.author,
      "quote": entity.quote,
      "date": entity.date
    }