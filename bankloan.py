def main():
    try:
        age = int(input("Enter your age: "))
        income = float(input("Enter your annual income (in shillings): "))

        if age >= 21 and income >= 21000:
            print("Congratulations! You qualify for a loan.")
        else:
            print("Unfortunately, we are unable to offer you a loan at this time.")
    except ValueError:
        print("Please enter valid numbers for age and income.")

if __name__ == "__main__":
    main()
