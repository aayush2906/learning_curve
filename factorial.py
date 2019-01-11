def factorial(n):
	if n>=1:
		value=n*factorial(n-1)
		return(value)
	else:
		return(1)
	
n=int(input("number::"))
print("Factorial is",+factorial(n))
