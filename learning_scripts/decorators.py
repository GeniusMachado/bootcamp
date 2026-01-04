def logger(a):
    def wrapper():		
	    print("logger started to log")
	    a()
	    print("logger ended the log")
    return wrapper

@logger
def testing():
	print("testing")

testing()

