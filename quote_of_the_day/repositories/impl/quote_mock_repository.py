from quote_of_the_day.entities.quote import Quote

from ..quote_repository import QuoteRepositoryInterface


class QuoteMockRepository(QuoteRepositoryInterface):
    def get_quote(self, quote_id) -> Quote:
        # TODO: the logic of fetching from persistence

        quote_entity = Quote(quote_id, 'My saved quote', 'My saved author')
        return quote_entity

    def create_quote(self, quote_data: Quote) -> Quote:
        # TODO: The logic of saving to persistence

        quote_entity = Quote('12345', quote_data.quote, quote_data.author)

        return quote_entity