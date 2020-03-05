from unittest import TestCase, main


class StockTest(TestCase):
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)


if __name__ == "__main__":
    main()
