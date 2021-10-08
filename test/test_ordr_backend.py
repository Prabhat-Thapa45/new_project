from src.order_backend import validate_entry, flower_out_of_stock, bq_size_exceeded


def test_validate_entry():
    for i in [1 , 3, 4.5]:
        assert validate_entry(i) == int(i)


def test_validate_entry_negative():
    for i in ['a', 0, -5]:
        assert validate_entry(i) is None


def test_flower_out_of_stock():
    order_quantity = 10
    in_stock = [11, 10]
    for i in in_stock:
        assert not flower_out_of_stock(order_quantity, i)
    in_stock = [9, 7]
    for i in in_stock:
        assert flower_out_of_stock(order_quantity, i)


def test_bq_size_exceeded():
