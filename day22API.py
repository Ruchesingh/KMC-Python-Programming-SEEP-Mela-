import requests

url = "https://markets.onlinekhabar.com/smtm/home/sector-performance"

r = requests.get(url=url)
if r.status_code == 200:
     data = r.json()
print(type(data))
print(data.keys())

result = data['response']
print(type(result))
for i in result:
        print(i['indices'] , i['percentage_change'])
else:
     print("Fail")

url = "https://markets.onlinekhabar.com/smtm/home/gainers-losers/Microfinance"
r = requests.get(url=url)
if r.status_code == 200:
    data = r.json()
    print(type(data))
    print(data.keys())
    data1 = data['response']
    print(type(data1))
    print(data1.keys())
    top_gainer = data1['topGainer']
    print(type(top_gainer))
    print(top_gainer['ticker_name'], top_gainer['ltp'])

    # top loser
    topLoser = data1['topLoser']
    print(type(topLoser))
    print(topLoser['ticker_name'], topLoser['ltp'])



else:
    print("Fail")