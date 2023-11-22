from inventory_report.product import Product


def test_create_product() -> None:
    product = Product("5", "gas mask", "amazon", "2023", "2027", "1035",
                      "store in dry spaces")

    assert product.id == "5"
    assert product.product_name == "gas mask"
    assert product.company_name == "amazon"
    assert product.manufacturing_date == "2023"
    assert product.expiration_date == "2027"
    assert product.serial_number == "1035"
    assert product.storage_instructions == "store in dry spaces"
