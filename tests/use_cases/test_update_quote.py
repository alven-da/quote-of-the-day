import unittest
from unittest.mock import MagicMock

from quote_of_the_day.use_cases.update_quote import UpdateQuoteUseCase
from quote_of_the_day.entities.quote import Quote
from quote_of_the_day.api.dtos import CreateOrUpdateQuoteDTO, QuoteOutputDTO

class TestUpdateQuoteUseCase(unittest.TestCase):
  def test_update_quote_success(self):
    apiPathId = '12345'
    apiInput = {
      'quote': 'My quote of the day',
      'author': 'Unknown'
    }

    mock_repo = MagicMock()
    mock_repo.update_quote.return_value = Quote(id=apiPathId, quote=apiInput.get('quote'), author=apiInput.get('author'))

    use_case = UpdateQuoteUseCase(mock_repo)
    dto = CreateOrUpdateQuoteDTO(author=apiInput.get('author'), quote=apiInput.get('quote'))

    result = use_case.execute(id=apiPathId, input=dto)

    self.assertEqual(result.id, apiPathId)
    self.assertEqual(result.quote, apiInput.get('quote'))
    self.assertEqual(result.author, apiInput.get('author'))