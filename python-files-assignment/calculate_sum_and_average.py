def calculate_sum_and_average():
    try:
        with open("number.txt", "r") as file:
            print("File opened successfully")
            total = 0
            count = 0
            for number in file:
                total += int(number.strip())
                count+= 1
            print(f"Read {count} numbers")
            print(f"Sum: {total}")
            print(f"Average: {total / count}")
            print("Processing completed")
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid number format in file")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculate_sum_and_average()
