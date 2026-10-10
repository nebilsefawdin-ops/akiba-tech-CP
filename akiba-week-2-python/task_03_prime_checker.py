num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    # We only check up to the square root of the number
    # because if a number has a divisor bigger than its square root,
    # it must also have a matching divisor smaller than its square root.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")