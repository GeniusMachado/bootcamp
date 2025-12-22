def readfile():
	for i in range(1000000):
		yield(i)

gen = readfile()
print(next(gen))
print(next(gen))
