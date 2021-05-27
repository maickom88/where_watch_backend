from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

INPUT = TypeVar('INPUT')
OUTPUT = TypeVar('OUTPUT')


class Usecase(Generic[INPUT, OUTPUT], ABC):
    @abstractmethod
    def call(self, input: INPUT) -> List[OUTPUT]:
        pass


class NoParams:
    pass
