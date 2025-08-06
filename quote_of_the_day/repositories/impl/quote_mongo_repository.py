from django.http import HttpResponseServerError
from bson import ObjectId

from quote_of_the_day.entities.quote import Quote
from ..quote_repository import QuoteRepositoryInterface
from ...infra.mongo.quote_model import QuoteDocument


class QuoteMongoRepository(QuoteRepositoryInterface):
    def get_quote(self, quote_id) -> Quote:
        try:
            obj_id = ObjectId(quote_id)
            doc = QuoteDocument.objects.get(id=obj_id)
            return Quote(str(doc.id), doc.quote, doc.author)
        except QuoteDocument.DoesNotExist:
            print("Document not found")
            return
        except Exception as e:
            print(f"Exception encountered: {e}")

    def create_quote(self, quote_data: Quote) -> Quote:
        doc = QuoteDocument(author=quote_data.author, quote=quote_data.quote)
        doc.save()
        return Quote(id=str(doc.id), quote=doc.quote, author=doc.author)
    
    def update_quote(slef, quote_data: Quote) -> Quote:
        obj_id = ObjectId(quote_data.id)
        doc = QuoteDocument.objects.get(id=obj_id)
        doc.update(
            set__author=quote_data.author,
            set__quote=quote_data.quote
        )

        doc.reload()

        return Quote(id=str(doc.id), quote=doc.quote, author=doc.author)



