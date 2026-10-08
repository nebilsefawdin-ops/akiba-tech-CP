num = int(input("Enter a positive number: "))

if num < 0:
    print("Please enter a positive number only")
elif num % 2 == 0:
    print("Even")
else:
    print("Odd")