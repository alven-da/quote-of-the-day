from rest_framework.views import APIView
from rest_framework.response import Response

from ..use_cases.create_quote_use_case import CreateQuoteUseCase
from ..api.dtos import CreateQuoteDTO
from ..repositories.impl.quote_mock_repository import QuoteMockRepository

class GetQuoteView(APIView):
  def get(self, request, id):
    return Response('GetQuote ' + id)

class HealthView(APIView):
  def get(self, request):
    return Response('Health Check')
  
class CreateQuoteView(APIView):
  def post(self, request):
    data = request.data
    author = data.get('author')
    quote = data.get('quote')

    input_dto = {
      "author": author,
      "quote": quote
    }

    dto = CreateQuoteDTO(**input_dto)

    repo = QuoteMockRepository()
    use_case = CreateQuoteUseCase(repo)
    response = use_case.execute(dto)

    return Response(response)
  

