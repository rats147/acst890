#creating a fibonacci sequence
	def fibonacci():
	num = int(input("How many numbers that generates?:")) 
	i = 1
	if num == 0:
  	fib = []          # generate an empty series
	elif num == 1: 
	  fib = [1] # first number prints
	elif num == 2: 
	  fib = [1,1] # this prints the first two numbers in the series in the formate [a,b]
	elif num > 2:  
	  fib = [1,1] # print the series in this format
	while i < (num - 1): 
	  fib.append(fib[i] + fib[i-1]) 
	   i += 1 
	return fib 
	print(fibonacci()) # print the series
	input() # this flashes the line to put the value
	
