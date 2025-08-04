print("Hello, my name is Bobby Brown your virtual assistant.I will helo you order a pizza")
userName = input("\nEnter your name:  ")
print(f"\Hello, {userName}. Nice to meet you!") 
size=input("\nWhat size pizza would you like? Enter small, medium, or large:  ")
flavor=input("\nWhat flavor of pizza?:  ")
crustType=input("\nWhat type of crust do you want:  ")
quantity=input("n\How many pizza(s) do you want to order? Enter numeric value:  ")
method=input("\nIs this pickup or delivery?:  ")
salesTax=1.1
pizzaCost=14.99
total = (14.99*4)*salesTax
print("-"*10)
print(f"Thank you, {userName}, for your order.  ")
print(f"your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs $({total:,.2f}."  )
print("-"*10)









