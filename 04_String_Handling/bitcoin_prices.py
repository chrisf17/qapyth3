from dateutil import parser
def get_price_lines():
    """
    Returns bitcoin prices
    :return: Price data as
    close,high,low,open,timestamp,volume
    """
    bitcoin_file = open("bitcoin_price.csv")
    keys = bitcoin_file.readline().rstrip().split(",")
    for idx,price_line in enumerate(bitcoin_file):
        yield price_line


