import bitcoin_prices as btc

# close,high,low,open,timestamp,volume
high = 0
low = None
volume = 0
close = 0
count = 0

volume = sum([float(f.split(',')[5]) for f in btc.get_price_lines()])
count = len([float(f.split(',')[0]) for f in btc.get_price_lines()])
high = max([float(f.split(',')[1]) for f in btc.get_price_lines()])
low = min([float(f.split(',')[2]) for f in btc.get_price_lines()])
average = sum([float(f.split(',')[0]) for f in btc.get_price_lines()])/count


print(f"Average Close Price:{average:20,.4f}")
print(f"High Price         :{high:20,.4f}")
print(f"Low Price          :{low:20,.4f}")
print(f"Volume             :{volume:20,.0f}")

