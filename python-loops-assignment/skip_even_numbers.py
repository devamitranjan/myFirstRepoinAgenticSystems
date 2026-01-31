def skip_even_numbers():
    for num in range(1, 11):
        if num % 2 == 0:
            continue
        print(num)

if __name__ == "__main__":
    skip_even_numbers()
