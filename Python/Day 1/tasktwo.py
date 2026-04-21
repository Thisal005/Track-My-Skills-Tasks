print("Temperature Converter")

option = input("Enter 1 to convert Celcius to Farenheit OR Enter 2 tp convert Farenheit to Celcius : ")
option = int(option)

if(option == 1):
    value = float(input("Enter Celcius : "))
    answer = (value * (9/5)) + 32
    print(f"Celcius {value} to Farenheit is {answer}")
elif(option == 2):
    value = float(input("Enter Farenheit : "))
    answer = (value - 32) * (5/9)
    print(f"Farenheit {value} to Celcius is {answer}")
else:
    print("Invalid Option!")
