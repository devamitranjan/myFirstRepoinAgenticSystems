def number_printer(n: int)-> None: 
    for num in range(n+1):
        print(num)

try:
    number = int(input("Enter the number:"))
    number_printer(number)
except ValueError:
    print("Invalid number! Please enter a valid integer number.")

