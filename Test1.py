month = input("In which month you have worked: ")

month=month.upper()

print(month)

salary = int(input("Enter salary: "))

if month == "JANUARY":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("You enter wrong days")

elif month== "FEBRUARY":

    day = 28

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("You Entered wrong days")

elif month== "MARCH":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("you entered wrong days try again")

    

elif month== "APRIL":

    day = 30

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else: 

        print("You have entered wrong days try again")

elif month== "MAY":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("You have entered wrong day")

elif month=="JUNE":

    day = 30

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("You have entered wrong days")

     

elif month== "JULY":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("you hve entered wrong days")

elif month== "AUGUST":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("you have entered wrong days")

elif month== "SEPTEMBER":

    day = 30

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("you have entered wrong days")

elif month== "OCTOBER":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("You have entered wrong days")

        

elif month== "NOVEMBER":

    day = 30

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("you have entered wrong days")

        

        

elif month== "DECEMBER":

    day = 31

    workDay= int(input("Enter how many days you have worked:"))

    if workDay<=day:

        totalAmount= workDay*salary

    else:

        print("wrong day")

while True:

    value = input("Enter value and type in formate D 200 or W 300: ")

    list1=value.split()

    type1 = list1[0]

    amount = int(list1[1])

    if type1 == "D" or type1== "d":

        totalAmount = amount+ totalAmount

        print("Total amout is: ", totalAmount)

    elif type1 == "W" or type1 =="w":

        if amount>totalAmount:

            print("You cant able to withdraw")

        else:

            totalAmount= totalAmount-amount

            print("Total amount remaining is: ", totalAmount)

    exitornot = input("You want to exit press Y else press N: ")

    if exitornot=="Y" or exitornot=="y":

        break
