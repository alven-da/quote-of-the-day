from rest_framework.views import APIView
from rest_framework.response import Response

from ..use_cases.create_quote import CreateQuoteUseCase
from ..use_cases.get_quote_by_id import GetQuoteByIdUseCase
from ..use_cases.update_quote import UpdateQuoteUseCase

from ..api.dtos import CreateOrUpdateQuoteDTO
from ..repositories.impl.quote_mongo_repository import QuoteMongoRepository

class GetQuoteView(APIView):
  # Get
  def get(self, request, id):
    repo = QuoteMongoRepository()
    use_case = GetQuoteByIdUseCase(repo)
    response = use_case.execute(id)

    return Response({
      'id': response.id,
      'author': response.author,
      'quote': response.quote
    })

  # Update
  def put(self, request, id):
    data = request.data
    repo = QuoteMongoRepository()
    use_case = UpdateQuoteUseCase(repo)

    input_dto = {
      'author': data.get('author'),
      'quote': data.get('quote')
    }

    dto = CreateOrUpdateQuoteDTO(**input_dto)

    resp = use_case.execute(id=id, input=dto)

    return Response({
      'id': resp.id,
      'author': resp.author,
      'quote': resp.quote
    })

class HealthView(APIView):
  def get(self, request):
    return Response('Health Check')
  
class CreateQuoteView(APIView):
  # Create
  def post(self, request):
    data = request.data

    input_dto = {
      'author': data.get('author'),
      'quote': data.get('quote')
    }

    dto = CreateOrUpdateQuoteDTO(**input_dto)

    repo = QuoteMongoRepository()
    use_case = CreateQuoteUseCase(repo)
    response = use_case.execute(dto)

    return Response({
      'id': response.id,
      'author': response.author,
      'quote': response.quote
    })