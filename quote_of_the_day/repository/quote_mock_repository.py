from quote_of_the_day.repository.quote_repository import QuoteRepository
from quote_of_the_day.core.entities import Quote

from datetime import date

class QuoteMockRepository(QuoteRepository):
  def get_quote_by_id(id):
    quote = Quote(id=id, quote="Yesterday is but today's memory, and tomorrow is today's dream", author="Anonymous", date="2025-07-25")
    return quote

# Format the date as YYYY-MM-DD
  def create_quote(quote: Quote):
    today = date.today()

    quote.id = 'randomly-generated-id'
    quote.date = today.strftime("%Y-%m-%d")

    return quote