# LEVEL - 1 - TASK - 2
temp=float(input("Enter temperature value:"))
unit=input("Enter unit (C or F):")
if unit =="C":
    F=temp*9/5+32
    print("The given temperature in fahrenheit is:",F)
elif unit=="F":
    C=(temp-32)*5/9
    print("The give temperature in celsius is:",C)
else:
    print("Invalid Unit! Please Enter 'C' or 'F'.")
