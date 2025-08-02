from django.http import HttpResponse

from rest_framework.decorators import api_view

from quote_of_the_day.core.quote_service import QuoteService
from quote_of_the_day.core.index_service import IndexService

import json

def home(request):
  welcome = IndexService.index()
  return HttpResponse(welcome)

@api_view(['GET'])
def get_quote_by_id(request, id):
  quote = QuoteService.get_quote_by_id(id)
  
  data = {
    "id": quote.id,
    "quote": quote.quote,
    "author": quote.author,
    "date": quote.date
  }

  json_string = json.dumps(data, indent=4)
  response = HttpResponse(json_string)
  response["Content-Type"] = "application/json"

  return response

@api_view(['POST'])
def create_quote(request):
  data = json.loads(request.body)

  resp = QuoteService.create_quote(data)

  json_string = json.dumps(resp, indent=2)

  response = HttpResponse(json_string)
  response["Content-Type"] = "application/json"

  return response
