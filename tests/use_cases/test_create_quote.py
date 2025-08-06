import unittest
from unittest.mock import MagicMock

from quote_of_the_day.use_cases.create_quote import CreateQuoteUseCase
from quote_of_the_day.entities.quote import Quote
from quote_of_the_day.api.dtos import CreateOrUpdateQuoteDTO

class TestCreateQuoteUseCase(unittest.TestCase):
  def test_create_quote_success(self):
    apiInput = {
      'quote': 'Create my quote of the day',
      'author': 'Unknown created'
    }

    mock_repo = MagicMock()
    mock_repo.create_quote.return_value = Quote(
      id='Newly generated quote',
      quote=apiInput.get('quote'),
      author=apiInput.get('author')
    )

    use_case = CreateQuoteUseCase(mock_repo)
    dto = CreateOrUpdateQuoteDTO(author=apiInput.get('author'), quote=apiInput.get('quote'))

    result = use_case.execute(dto)

    self.assertEqual(result.id, 'Newly generated quote')
    self.assertEqual(result.quote, apiInput.get('quote'))
    self.assertEqual(result.author, apiInput.get('author'))