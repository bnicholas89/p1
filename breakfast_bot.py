print("Hello! I am Bob, the Breakfast Bot.") # All of these are outside the loop.
print("Today we have two breakfasts available.")
print("The first is waffles with strawberries and whipped cream.")
print("The second is sweet potato pancakes with butter and syrup.")
while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")
print("Your order will be ready shortly.") # This one is also outside the loop!