from abc import abstractmethod, ABC
from typing import Any
from house import House
from pieces.piece import Piece


class Grid(ABC):

    @abstractmethod
    def get_content(self, house: House) -> Piece:
        pass

    @abstractmethod
    def is_empty(self, house: House):
        pass

    @abstractmethod 
    def remove_content(self, house: House):
        pass

    @abstractmethod
    def add_content(self, location: House, content: Any):
        pass

    @abstractmethod
    def move_content(self, source: House, destination: House):
        pass

    @abstractmethod
    def is_valid_house(self, house: House):
        pass

    @abstractmethod
    def print(self):
        pass