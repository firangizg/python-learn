first_number = input("First number? ")

if first_number.isnumeric() == False:
    print("Please input a number.")
    exit()

operation = input("Operation? ")


second_number = input("Second number? ")

if second_number.isnumeric() == False:
    print("Please input a number.")
    exit()

x = int(first_number)
y = int(second_number)

result = 0 

if operation == '+':
    result = x + y
    label = 'Sum'
elif operation == '-':
    result = x - y
    label = 'Difference'
elif operation == '*':
    result = x * y
    label = 'Product'
elif operation == '/':
    result = x / y
    label = 'Quotient'
elif operation == '**':
    result = x ** y
    label = 'Exponent'
elif operation == '%':
    result = x % y
    label = 'Modulus'
else:
     print("Operation not recognized.")
     exit()

print(f"{label} of {first_number} {operation} {second_number} equals {result}")
