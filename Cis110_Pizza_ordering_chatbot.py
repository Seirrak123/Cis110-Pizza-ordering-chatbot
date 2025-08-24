print("Hello, my name is Bobby Brown your virtual assistant.I will helo you order a pizza!")
print("Im going to ask a few questions , press enter after answer")

userName = input("\nEnter your name:  ")
while len (userName) == 0 :
    userName = input("Name cannot be blank! Please enter your name:  ")

if userName.lower() == "Seirra King":
    print(f"\nMy creator, (userName). Pleasure to serve you!")
else:
    print(f"\nHello, (userName). Nice to meet you!")

    keepGoing = "y"
    while keepGoing.lower() == "y":

         size=input("What size pizza would you like? Enter small, medium, or large:  ")
         size=input("Invalid value! Please enter small, medium, or large:  ")

    flavor=input("What flavor of pizza?:  "
         while len(flavor) == 0:
          flavor = input("flavor cannot be blank! Please enter a flavor:  ")

        crustType=input("What type of crust do you want:  ")
        while len(crustType) == 0:
            crustType = input("crust type cannot be blank! please enter crust type:  ")

        quantity=input("How many pizza(s) do you want to order? Enter numeric value:  ")
    
        while not quantity.isdigits():
            quantity=input("\nValue not recognized. Please enter a numeric value:  ")
    
    quantity=int(quantity)

    method=input("Is this pickup or delivery:  ")
    while method not in ["pickup","delivery"]:
        method=input("Invalid value! Please enter a pickup or delivery:  ")

    if method.lower() == "delivery":
        deliveryFee =5
        print("$5 delivery fee has been added to order,  ")
    else: 
        deliveryFee =0
        print("pickup selected, no delivery fee.")

    salesTax= 1.1

    if size.lower() == "small":
       pizzaCost= 8.99
    elif size.lower() == "medium":
       pizzaCost= 14.99
    elif size.lower() == "large":
        pizzaCost= 17.99

    total = (pizzaCost * quantity) * salesTax + deliveryFee

    print("-"*10)
    print(f"Thank you, {userName}, for your order.  ")
    print(f"your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs $({total:,.2f}."  )

    if total >= 50:
      print("\nCongradulations!You have been awarded $10 off coupon for your next order.  ")
    else:
       print("\nOrder over $50 will receive $10 off coupon!  ")


    print("order has been recieved. ETA 3 mins!")
    for min in range(3, 0, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0 , -1):
            print(seconds, end = "\r")
            import time
            time.sleep(1)
    print("order is ready!")

keepGoing = input("Do you want to place another order? Enter y or no:  ")
while keepGoing.lower() not in ["y", "n"]:
     keepGoing=input("Invalid value: Enter y or n:")

