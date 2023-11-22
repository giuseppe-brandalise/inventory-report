from inventory_report.product import Product
from typing import Optional


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        if data:
            self.__data = data
        else:
            self.__data = []

    @property
    def data(self):
        return self.__data

    def add_data(self, data: list[Product]):
        self.__data.extend(data)
