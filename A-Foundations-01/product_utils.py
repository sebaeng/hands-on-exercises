PRODUCT_FORMAT = "name:price:quantity"


def calculate_total_price(products):
    """Calculate the total price of a list of products.

    Each product must be a dict with numeric 'price' and 'quantity' keys.
    Invalid or missing entries are skipped.

    Args:
        products: list of product dicts.

    Returns:
        Total price as a float, or 0 if the list is empty or all entries are invalid.
    """
    if not products:
        return 0

    total = 0.0
    for product in products:
        if not isinstance(product, dict):
            continue

        price = product.get("price", 0)
        quantity = product.get("quantity", 0)

        if not isinstance(price, (int, float)) or not isinstance(quantity, (int, float)):
            continue

        total += price * quantity

    return total


def parse_product_arg(raw_arg):
    """Parse a command-line argument into a product dict.

    Args:
        raw_arg: string in the format 'name:price:quantity'.

    Returns:
        A product dict, or None if the format is invalid.
    """
    try:
        name, raw_price, raw_quantity = raw_arg.split(":")
        return {
            "name": name,
            "price": float(raw_price),
            "quantity": int(raw_quantity),
        }
    except ValueError:
        return None


def print_usage():
    print(f"Usage: python product_utils.py <product1> [product2 ...]")
    print(f"Each product must follow the format: '{PRODUCT_FORMAT}'")
    print(f"Example: python product_utils.py apple:1.50:3 banana:0.75:5")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    products = []
    for arg in sys.argv[1:]:
        product = parse_product_arg(arg)
        if product is None:
            print(f"Skipping invalid entry '{arg}' — expected format: '{PRODUCT_FORMAT}'")
        else:
            products.append(product)

    total_price = calculate_total_price(products)
    print(f"Total price: {total_price:.2f}")
