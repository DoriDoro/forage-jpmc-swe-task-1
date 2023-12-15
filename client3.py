################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def get_data_point(single_quote):
    """Produce all the needed values to generate a datapoint"""

    data_stock = single_quote["stock"]
    data_bid_price = float(single_quote["top_bid"]["price"])
    data_ask_price = float(single_quote["top_ask"]["price"])
    data_price = round((data_bid_price + data_ask_price) / 2, 2)

    # check if single_quote["top_bid"]["price"] or single_quote["top_ask"]["price"] is 0, None or NaN:
    for s_q in single_quote.values():
        if isinstance(s_q, dict):
            for value in s_q.values():
                if value is None:
                    raise ValueError(f"{value} is not defined.")
                if value == 0:
                    raise ValueError(f"{s_q} value: {value} is 0.")
                if not isinstance(value, (int, float)):
                    raise ValueError(f"{value} is not a number.")

    return data_stock, data_bid_price, data_ask_price, data_price


def get_ratio(price_a, price_b):
    """Get ratio of price_a and price_b"""

    return round(price_a / price_b, 4) if price_b else 0


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(
            urllib.request.urlopen(QUERY.format(random.random())).read()
        )

        all_prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = get_data_point(quote)
            all_prices[stock] = price
            print(
                "Quoted %s at (bid:%s, ask:%s, price:%s)"
                % (stock, bid_price, ask_price, price)
            )

        print("Ratio %s" % get_ratio(all_prices["ABC"], all_prices["DEF"]))
