#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill = input("how much is your bill ? $ ")
persons = input("Between how many members you want to split the bill ? ")
tip = input("please enter tip percentage 10,15 or 20 : ")
# total_tip = int(bill) * int(tip) / 100
# total_bill = float(bill) + float(total_tip)
total = float(bill) * int(tip) / 100 + float(bill)
individual_bill = float(total) / int(persons)
individual_bill = "{:.2f}".format(individual_bill)
print(f"Individual person should pay {individual_bill}")
