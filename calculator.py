#calculator

#calculation function
def calculate():
	signs = "+-*x/%"

	filter_sign = ''.join([

		s
		for s in equation
		if s in signs

		])


	number = [
		int(num) 
		for num in equation.split(filter_sign) 
		if num.isdigit()

		]




	if filter_sign == '+':   
	    result = number[0] + number[1]

	elif filter_sign == '-':    
	    result = number[0] - number[1]

	elif filter_sign == '*':
	    result = number[0] * number[1]

	elif filter_sign == 'x':
	    result = number[0] * number[1]

	elif filter_sign == '/':
	    result = number[0] / number[1]

	elif filter_sign == '%':
	    result = number[0] % number[1]


	print('The result is : ' + str(result))


# main function
i = 1
while i > 0:
	equation = input("\nEnter your Equation(enter 0 to exit): ")


	if equation == '0':
		break

	calculate()
