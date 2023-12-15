import unittest
from client3 import get_data_point


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(
                get_data_point(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    ((quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2),
                ),
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(
                get_data_point(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    ((quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2),
                ),
            )

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_askPriceIsZero(self):
        quotes = [
            {
                "top_ask": {"price": 0, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 0, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        for quote in quotes:
            get_data_point(quote)
            self.assertEquals(quote["top_ask"]["price"], 0)

    def test_getDataPoint_raiseErrorForInvalidInput(self):
        quotes = [
            {
                "top_ask": {"price": 0, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
            },
            {
                "top_ask": {"price": 0, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
            },
        ]
        for quote in quotes:
            with self.assertRaises(KeyError):
                get_data_point(quote)

    def test_getDataPoint_raiseErrorForNonNumericPrice(self):
        quotes = [
            {
                "top_ask": {"price": "some string", "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": "some string", "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        for quote in quotes:
            with self.assertRaises(ValueError):
                get_data_point(quote)


if __name__ == "__main__":
    unittest.main()
