def sum_until_zero():
    total = 0
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        total += num
    print(f"Total: {total}")

if __name__ == "__main__":
    try:
        sum_until_zero()
    except ValueError:
        print("Invalid input. Please enter integers only.")
