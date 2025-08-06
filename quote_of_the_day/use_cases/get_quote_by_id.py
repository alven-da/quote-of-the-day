from quote_of_the_day.api.dtos import QuoteOutputDTO
from ..repositories.quote_repository import QuoteRepositoryInterface
from ..entities.quote import Quote

class GetQuoteByIdUseCase():
  def __init__(self, quote_repository: QuoteRepositoryInterface):
    self.quote_repository = quote_repository

  def execute(self, id: str):
    # The response expects the ID is already generated
    quote_response = self.quote_repository.get_quote(id)

    return QuoteOutputDTO(
      id=quote_response.id,
      author=quote_response.author,
      quote=quote_response.quote
    )