from quote_of_the_day.api.dtos import CreateQuoteDTO
from ..repositories.quote_repository import QuoteRepositoryInterface
from ..entities.quote import Quote

class CreateQuoteUseCase():
  def __init__(self, quote_repository: QuoteRepositoryInterface):
    self.quote_repository = quote_repository

  def execute(self, input: CreateQuoteDTO):
    
    quote_entity = Quote('', input.quote, input.author)

    # The response expects the ID is already generated
    quote_response = self.quote_repository.create_quote(quote_entity)

    return {
      "id": quote_response.id,
      "author": quote_response.author,
      "quote": quote_response.quote
    }