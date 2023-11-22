from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        return (
            f"{super().generate()}\n"
            f"{self.get_companies_stocked()}"
        )

    def get_companies_stocked(self) -> str:
        company_stocked: dict[str, int] = {}

        for inventory in self.inventory:
            for product in inventory.data:
                if product.company_name in company_stocked:
                    company_stocked[product.company_name] += 1
                else:
                    company_stocked[product.company_name] = 1

        amount_per_company = "Stocked products by company:\n"

        for company, stocked in company_stocked.items():
            amount_per_company += f"- {company}: {stocked}\n"

        return amount_per_company
