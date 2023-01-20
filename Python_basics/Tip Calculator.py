#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("Enter the total bill: "))
rate = 1+(int(input("How much tip would you like to give? 10, 12, or 15? "))/100)
no_of_people = int(input("How many people to split the bill? "))
per_head_cost = (total_bill/no_of_people)*rate
print("{:.2f}".format(round(per_head_cost,2)))
