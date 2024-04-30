from abc import ABC, abstractmethod

from house import House

class Piece(ABC):

    @abstractmethod
    def set_location(self, destination: House):
        pass

    @abstractmethod
    def get_legal_moves_position(self, destination: House):
        pass