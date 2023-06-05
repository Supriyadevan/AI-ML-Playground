try:
    TotalValue = float(input("Enter total value: "))
    Value = float(input("Enter value: "))
    try:
        Percentage = Value/TotalValue * 100
        print("Percentage: ", Percentage,'%')
    except ZeroDivisionError:
        print("Total value cannot be Zero")

except ValueError:
    print("You need to enter a number. Run the program again. ")







