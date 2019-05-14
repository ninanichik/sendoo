from abc import ABC, abstractmethod


class BasePage(ABC):
    @abstractmethod
    def open(self, driver) -> None:
        pass

    @abstractmethod
    def loaded(self) -> bool:
        pass
