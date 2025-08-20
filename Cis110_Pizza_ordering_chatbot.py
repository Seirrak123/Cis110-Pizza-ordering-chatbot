print("Hello, my name is Bobby Brown your virtual assistant.I will helo you order a pizza")
userName = input("\nEnter your name:  ")
while len(userName) ==0:
    userName = input("please enter your name:")
if userName.lower() == "seirra king":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")
    size=input("\nWhat size pizza would you like? Enter small, medium, or large:  ")
    flavor=input("\nWhat flavor of pizza?:  ")
    flavor=input("Please enter a flavor: ")
    crustType=input("\nWhat type of crust do you want:  ")
quantity=input("n\How many pizza(s) do you want to order? Enter numeric value:  ")
while not quantity. isdigit():
 quantity=int(quantity)
 method=input("\nIs this pickup or delivery?:  ")
 while method not in ["pickup","delivery"]:
       method = input("please enter pickup or delivery: ")

 if .lower() == "delivery":
   deliveryFee =5
else:
   deliveryFee =0
salesTax=1.1

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
   print("-"*10)