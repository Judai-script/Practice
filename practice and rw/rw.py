from alpha_vantage.fundamentaldata import FundamentalData
key_path = "C:/Users/patel/OneDrive/Desktop/top secret.txt"
with open(key_path, "r") as f:
    dakey = f.read()
    dakey = dakey[23:]
fd = FundamentalData(key=dakey, output_format="pandas")
print(fd.get_balance_sheet_annual("AAPL"))