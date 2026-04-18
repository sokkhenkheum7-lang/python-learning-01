hour = int (input("Enter your time in 24 hour format: "))
if hour < 0 or hour >= 24:
    print("Invalid time")
elif hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good evening")