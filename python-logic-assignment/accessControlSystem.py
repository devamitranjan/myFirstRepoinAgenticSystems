def accessControlSystem(age: int, has_id: bool):
    if age >=18  and has_id:
        print("Entry allowed")
    else:
        print("Entry not allowed")

def parseBoolean(value: str) -> bool:
    value = value.strip().lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("Verification status must be True/False")

try:
    age = int(input("Age:"))
    has_id_input = input("Has ID:")
    has_id = parse_boolean(has_id_input)
    accessControlSystem(age, has_id)
except ValueError as e:
    print(f"Invalid input: {e}")