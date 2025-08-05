from abc import ABC, abstractmethod

from ..entities.quote import Quote

class QuoteRepositoryInterface(ABC):
    @abstractmethod
    def get_quote(self, quote_id) -> Quote:
        pass

    @abstractmethod
    def create_quote(self, quote_data: Quote) -> Quote:
        pass