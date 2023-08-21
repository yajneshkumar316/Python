# Program to print the given year is leap year or not
print("This program will check whether the entered year is leap year or not.\n")
year = int(input("Enter the you want to check: "))
if year%4 == 0:
    if year%100 != 0:
        print(f"{year} is a leap year.")
    else: 
        if year%400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year")
else: 
    print(f"{year} is not a leap")
