def secureTransactionValidator(balance: int, withdrawal: int, verified: bool):
    if verified and withdrawal <= balance:
        print("Withdrawal successful")
    else:
        print("Transaction denied")


def parseBoolean(value: str) -> bool:
    value = value.strip().lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("Verification status must be True/False")


try:
    balance = int(input("Account balance: "))
    withdrawal = int(input("Withdrawal amount: "))
    verified_input = input("Verification status (True/False): ")
    verified = parseBoolean(verified_input)

    secureTransactionValidator(balance, withdrawal, verified)

except ValueError as e:
    print(f"Invalid input: {e}")