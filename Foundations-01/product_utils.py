# Create a Python function that calculates the total price of a list of products.
# Handle these cases: empty product list, invalid values
def calculate_total_price(products):
    if not products:
        return 0
    total_price = 0
    for product in products:
        if not isinstance(product, dict):
            continue
        price = product.get('price', 0)
        quantity = product.get('quantity', 0)
        if not isinstance(price, (int, float)) or not isinstance(quantity, (int, float)):
            continue
        total_price += price * quantity
    return total_price

# Take a list of products from command line with the format "name:price:quantity" and calculate the total price using the function above.
# Add usage if invoked without parameters or with invalid parameters.
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python product_utils.py <product1> <product2> ...")
        print("Each product should be in the format 'name:price:quantity'")
        sys.exit(1)
    products = []
    for arg in sys.argv[1:]:
        try:
            name, price, quantity = arg.split(':')
            products.append({'name': name, 'price': float(price), 'quantity': int(quantity)})
        except ValueError:
            print(f"Invalid product format: {arg}. Expected format is 'name:price:quantity'. Skipping.")
    total = calculate_total_price(products)
    print(f"Total price of products: {total}")
