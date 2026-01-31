print("--- Quick Inch to CM Converter ---")
print("Type a negative number when you're done.")

while True:
    inches = float(input("\nInches: "))

    if inches < 0:
        print("Catch you later!")
        break

    cm = inches * 2.54
    print(f"That's {cm:.2f} cm")
