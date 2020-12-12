temp = input("What's the temperature in fahrenheit?: ")

if temp.isnumeric() == False: 
    print("Please enter a number.")
    exit()

fahrenheit = int(temp)
celsius = int((fahrenheit - 32) * 5/9)

print("Temperature in celsius is: " + str(celsius))