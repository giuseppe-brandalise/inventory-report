from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import json
from csv import DictReader


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            json_data = json.load(file)
        products_list = [Product(**product) for product in json_data]
        return products_list


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            csv_data = DictReader(file)
            products_list = [Product(**product) for product in csv_data]
        return products_list


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
