def find_first_multiple_of_7():
    for num in range(1, 51):
        if num % 7 == 0:
            print(num)
            break

if __name__ == "__main__":
    find_first_multiple_of_7()
