import urllib.request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1537327480&period2=1539919480&interval=1d&events=history&crumb=GEuoQZkGpt2'
urllib.request.urlretrieve(goog_url, "Goog.csv")


def download(url):
    with urllib.request.urlopen(url) as response:
        csv = response.read()
    #csv = response.read()
    #csv_str = str(csv)
    lines = str(csv).split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

#download(goog_url)