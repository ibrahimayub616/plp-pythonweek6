def get_number():
    try:
        number = int(input("Enter a whole number: "))
        return number
    except ValueError:
        return "Not a valid number"


print(get_number())
print("Program is still running!")