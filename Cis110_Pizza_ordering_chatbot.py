print("Hello, my name is Bobby Brown your virtual assistant.I will helo you order a pizza")
userName = input("\nEnter your name:  ")
while len {userName} == 0 :
    userName = input("Name cannot be blank! Please enter your name:  ")

if userName.lower() == "seirra king":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")

    size=input("What size pizza would you like? Enter small, medium, or large:  ")
    flavor=input("What flavor of pizza?:  ")
    crustType=input("What type of crust do you want:  ")
    quantity=input("How many pizza(s) do you want to order? Enter numeric value:  ")
    method=input("Is this pickup or delivery:  ").lower()
if:  
   deliveryFee =5
else:
   deliveryFee =0
if size.lower() == "small":
   pizzaCost= 8.99
elif size.lower() == "medium":
   pizzaCost= 14.99
elif size.lower() == "large":
    pizzaCost= 17.99

salesTax=1.1

total = (pizzaCost * quantity) * (1+salesTax) + deliveryFee
print(f"Your total is: ${total:.2f}")
print("-"*10)
print(f"Thank you, {userName}, for your order.  ")
print(f"your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs $({total:,.2f}."  )
if total >= 50:
  print("\nCongradulations!You have been awarded $10 off coupon for your next order.  ")
else:
   print("\nOrder over $50 will receive $10 off coupon!  ")
   print("-"*10)

