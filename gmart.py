def take_orders(customer_name, order_items, products, amount):
    
    order_details = {
        "customer_name": customer_name,
        "order_items": order_items,
        "products": products,
        'amount': amount
    }
    return order_details


# create an instance of the order
order = take_orders("John Doe", ["Apples", "Bananas"], ["Apples", "Bananas", "Oranges"], 25.50)


print(order)