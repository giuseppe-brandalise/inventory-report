from inventory_report.inventory import Inventory
from datetime import date


class SimpleReport:
    def __init__(self) -> None:
        self.inventory: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory.append(inventory)

    def generate(self):
        company = self.get_company()
        expiration = self.get_expiration()
        manufacturing = self.get_manufacturing()

        return (
            f"Oldest manufacturing date: {manufacturing}"
            f"Closest expiration date: {expiration}"
            f"Company with the largest inventory: {company}"
        )

    def get_manufacturing(self):
        searched_date = "9999-99-99"

        for inventory in self.inventory:
            for product in inventory.data:
                if product.manufacturing_date < searched_date:
                    searched_date = product.manufacturing_date

        return searched_date

    def get_expiration(self):
        searched_date = "9999-99-99"

        for inventory in self.inventory:
            for product in inventory.data:
                if (
                    product.expiration_date >= str(date.today()) and
                    product.expiration_date < searched_date
                ):
                    searched_date = product.expiration_date

        return searched_date

    def get_company(self):
        companies = []
        for inventory in self.inventory:
            for product in inventory.data:
                companies.append(product.company_name)
        company_max = max(
            companies,
            key=companies.count)
        return company_max
