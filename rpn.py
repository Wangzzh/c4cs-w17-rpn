#! usr/bin/env python3

def calculate(arg):
	stack = []
	tokens = arg.split(' ')
	for operand in tokens:
		try:
			operand = float(operand)
			stack.append(operand)
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			if operand == '+':
				stack.append(arg1 + arg2)
			elif operand == '-':
				stack.append(arg1 - arg2)
	return stack.pop()

def main():
	while True:
		print("Result:", calculate(input("rpn calc>")))

if __name__ == "__main__":
	main()
