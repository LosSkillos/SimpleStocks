import yfinance as yf
import matplotlib.pyplot as plt
import threading
#sort(reverse = True)


def stockfind(stockcodes, times):
	company_days = []
	company_stock = []
	company_names = []
	for symbol in stockcodes.split(" "):
		msft = yf.Ticker(symbol)
		print(msft.info)
		hist = msft.history(period=times)
		time = []
		position = []
		for day, value in enumerate(hist["Open"]):
			print("%d: %d" % (int(day), int(value)))
			time.append(day)
			position.append(value)
		company_days.append(time)
		company_stock.append(position)
		company_names.append(msft.info["shortName"])
	company_exist = []
	for existence in company_days:
		company_exist.append(len(existence))
	print(company_exist)
	company_exist.sort(reverse = True)
	print(company_exist)
	longest = company_exist[0]
	for exist in company_exist:
		print("Exist: %d" % exist)
		for num, x in enumerate(company_days):
			print("Num: %d" % num)
			xln = len(x)
			if xln == exist:
				for a in range(longest - xln):
					company_days[num].append(len(company_days[num]) + 1)
					company_stock[num].insert(0, 0)
				print(company_days[num])
				print(company_stock[num])
				plt.plot(company_days[num], company_stock[num], label=company_names[num]) 

	#plt.title("Stock price of %s" % (msft.info["shortName"]))
	#plt.plot(time, position)
	plt.xlabel('Time (DAY)')
	plt.ylabel("Stock price (USD)")
	plt.title("Stock Comparsion")
	plt.legend()
	plt.show()

print("Hint: ") 
print("Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max")
stockfind(input("Symbols: "), input("Timespace: "))


