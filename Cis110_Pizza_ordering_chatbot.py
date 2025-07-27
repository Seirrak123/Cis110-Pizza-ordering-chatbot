print("my name is seirra and im your virutal assistant. i will help you order your pizza!")

username=input("\nEnter your name:  ")
print(f"\nHello,  {username}. Nice to meet you!")
size=input("\nwhat size do you want? Enter small medium or large:  ")
flavor=input("\nEnter the flavor of pizza:  ")
crusttype=input("n\what type of crust do yo want:  ")
quantity=input("n\How many of those you want:#:  ")
method=input("n\Is this pick up or delivery:  ")
salestax=1.1 
pizzacost=14.99
total=(14.99*4)*1.1
quantity=input("\nHow many of those you want? : # :  ")
quantity=int(quantity)
print("-"*10)
print(f"thank you, {username}, for your order.") 
print(f"your {quantity} {size} {flavor} pizza(s) with {crusttype} crust cost ${total:.2f}:")
print("-" * 10)


