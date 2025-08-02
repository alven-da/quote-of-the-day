from abc import ABC, abstractmethod


class QuoteRepository(ABC):
  @abstractmethod
  def get_quote_by_id(id): pass