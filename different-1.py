
while True:
	try:
		# Reads two numbers from input and typecasts them to int using  
		# list comprehension, invalid input will throw an exception which
		# the block will catch and then break out of the loop 
		x, y = [int(x) for x in input().split()] 

		# If the input is valid print the absolute result
		print(abs(x - y))
	except:
		break
