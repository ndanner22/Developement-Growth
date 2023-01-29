# import the math library
import math

# request user input either 'bond' or 'investment' and save as string variable user_invest
print("Chose either 'investment' or 'bond' from the menu below to proceed:")
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()
user_invest = input()
# convert user_invest to all lower case
user_invest = str.lower(user_invest)
print()

# create an if statement that checks if user_invest is 'investment'
if user_invest == "investment":
	# request user to input how much money they are investing and save into variable deposit
	deposit = float(input("How much money are you investing? "))
	# request user input what the interest rate is and save into varirable int_rate
	int_rate = float(input("What is the interest rate (please do not enter a '%' symbol)? "))
	# set int_rate equal to int_rate divded by 100 to get interest rate in decimal form
	int_rate = int_rate/100
	# request user to input how many years they will invest and save as variable years
	years = int(input("How many years do you plan on investing for? "))
	# request user to input whether they will have simple or compound interest and save as int_type
	int_type = input("Would you like 'simple' or 'compound' interest? ")
	# convert int_type into all lower case
	int_type = str.lower(int_type)
	
	# create an if statement to check if int_type is 'simple'
	if int_type == "simple":
		# create varialbe inv_tot and set equal deposit * (1 + int_rate*years) simple interest formula
		inv_tot = deposit*(1+int_rate*years)
		# round inv_tot to two decimal places
		inv_tot = round(inv_tot,2)
		print()
		# print inv_tot with a sentence that says "At the end of your investment you would have...'
		print(f"At the end of your investment you would have R{inv_tot}.")
	# create elif statement to check if int_type is 'compound'
	elif int_type == "compound":
		# create variable inv_tot and set equal to deposit (1+int_rate^*years) compound interest formula
		inv_tot = deposit*math.pow((1+int_rate),years)
		# round inv_tot to two decimal points
		inv_tot = round(inv_tot, 2)
		print()
		# print inv_tot with a sentence that says 'At the end end of your investment you would have...'
		print(f"At the end of your investment you would have R{inv_tot}.")
	# create an else statement that prints out 'Please choose simple or compound'
	else:
		print()
		print("Please try again and choose 'simple or 'compound'.")

# create an elif statement to check if user_invest is bond
elif user_invest == "bond":
	# request user to input the value of their house and save as variable val_house
	val_house = float(input("What is the present value of your house? "))
	# request user to input their interst rate and save as int_rate
	int_rate = float(input("What is your interest rate? "))
	# set int_rate equal to int_rate/100 to get intrest rate in decimal form
	int_rate = int_rate / 100
	# divide int_rate by 12 and save as variable int_month to get monthly interest rate
	int_month = int_rate / 12
	# request user to input how many months they will repay the bond in and save as variable months
	months = int(input("How many months will it take to repay the bond? "))
	# set months equal to months multiplied by -1 to set the value as a negative integer
	months = -1 * months
	# create variable pay_month and set it to (int_month * val_house)/(1 - (1+int_month)^(months)) bond repayment formula
	pay_month = (int_month*val_house)/(1 - math.pow((1+int_month), months))
	# round pay_month to two decimal points
	pay_month = round(pay_month,2)
	print()
	# print out pay_month with the sentence 'Your monthly payment will be...'
	print(f"Your monthly payment will be R{pay_month}.")
else:
	print("Please try again and select either 'investment' or 'bond'.")
	