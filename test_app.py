from gmart import take_orders


def test_take_orders():
    result = take_orders(
        "John Doe",
        ["Apples", "Bananas"],
        ["Apples", "Bananas", "Oranges"],
        25.50
    )

    assert result == {
        "customer_name": "John Doe",
        "order_items": ["Apples", "Bananas"],
        "products": ["Apples", "Bananas", "Oranges"],
        "amount": 25.50
    }