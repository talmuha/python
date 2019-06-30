print ("""WELCOME TO THE QUICK CALCULATOR!""")
print ("Insert two whole numbers then choose an operation from the following list")


#INPUTTING THE NUMBERS TO BE CALCULATED
print ("YOUR FIRST NUMBER, PLEASE:")
num_1 = input()
print ("YOUR SECOND NUMBER, PLEASE:")
num_2 = input()

#INPUTTING THE MATHEMATICAL OPERATION
print (" Choose a mathematical operation from the list(+, -, /, *)  PLEASE:")
math_op = input()

if num_1.isdigit() and num_2.isdigit():

	print ("Perfect! Now we can do math.")

if math_op == "+":
	solution = int(num_1) + int(num_2)

	print ("you have chosen a:" + math_op + ", and your solution is:" + str(solution))

elif math_op == "-":
	solution = int(num_1)- int(num_2)

	print ("you have chosen a:" + math_op + ", and your solution is:" + str(solution))

elif math_op == "*":
	solution = int(num_1) * int(num_2)

	print ("you have chosen a:" + math_op + ", and your solution is:" + str(solution))

elif math_op == "/":
	solution = int(num_1) / int(num_2)

	print ("you have chosen a:" + math_op + ", and your solution is:" + str(solution))

else:

	print ("It seems you haven't entered values, exiting")

