import bitcoin_prices as btc


for line in btc.get_price_lines():
    print(line[:-1])