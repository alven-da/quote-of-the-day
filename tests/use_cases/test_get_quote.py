import unittest
from unittest.mock import MagicMock

from quote_of_the_day.use_cases.get_quote_by_id import GetQuoteByIdUseCase
from quote_of_the_day.entities.quote import Quote
from quote_of_the_day.api.dtos import CreateOrUpdateQuoteDTO

class TestCreateQuoteUseCase(unittest.TestCase):
  def mock_find_in_array(self, strId: str):
    quote_records = [
      Quote(id='12345', quote='Test quote 1', author='Test author 1'),
      Quote(id='24680', quote='Test quote 2', author='Test author 2')
    ]

    for i in range(len(quote_records)):
      if quote_records[i].id == strId:
          return quote_records[i]
    return None

  def test_create_quote_success(self):
    apiInputId: str = '12345'

    mock_repo = MagicMock()
    mock_repo.get_quote.return_value = self.mock_find_in_array(apiInputId)

    use_case = GetQuoteByIdUseCase(mock_repo)

    result = use_case.execute(apiInputId)

    self.assertEqual(result.id, '12345')
    self.assertEqual(result.quote, 'Test quote 1')
    self.assertEqual(result.author, 'Test author 1')