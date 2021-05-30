from abc import ABC, abstractmethod
from typing import TypeVar, Generic

INPUT = TypeVar('INPUT')
OUTPUT = TypeVar('OUTPUT')


class Usecase(Generic[INPUT, OUTPUT], ABC):
    @abstractmethod
    def call(self, input: INPUT) -> OUTPUT:
        pass


class NoParams:
    pass
