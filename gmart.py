def take_orders(customer_name, order_items, products, amount):
    """
    Function to take orders from customers.

    Parameters:
    customer_name (str): Name of the customer placing the order.
    order_items (list): List of items being ordered.

    Returns:
    dict: A dictionary containing the customer's name and their order details.
    """
    order_details = {
        "customer_name": customer_name,
        "order_items": order_items,
        "products": products,
        'amount': amount
    }
    return order_details

order = take_orders("John Doe", ["Apples", "Bananas"], ["Apples", "Bananas", "Oranges"], 25.50)


print(order)