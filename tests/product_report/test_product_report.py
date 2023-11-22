from inventory_report.product import Product


def test_product_report() -> None:
    product = Product("5", "gas mask", "amazon", "2023", "2027", "1035",
                      "store in dry spaces")

    assert (
        str(product)
        == "The product 5 - gas mask "
        "with serial number 1035 "
        "manufactured on 2023 "
        "by the company amazon "
        "valid until 2027 "
        "must be stored according to the following instructions: "
        "store in dry spaces."
    )
