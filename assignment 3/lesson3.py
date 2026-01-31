print("Enter your numbers below. Just hit Enter on an empty line to finish.")

largest = None
smallest = None

while True:
    user_input = input("Number: ")

    if user_input == "":
        break

    try:
        num = float(user_input)

        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num

    except ValueError:
        print("That wasn't a number. Try again!")

if largest is not None:
    print(f"\nResults:\nSmallest: {smallest}\nLargest: {largest}")
else:
    print("\nYou didn't enter any numbers!")
