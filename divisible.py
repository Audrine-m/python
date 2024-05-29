def main():
    try:
        number = int(input("Enter a number: "))
        
        divisible_by_5 = number % 5 == 0
        divisible_by_7 = number % 7 == 0
        divisible_by_11 = number % 11 == 0
        is_even = number % 2 == 0
        
        if divisible_by_5:
            print(number, "is divisible by 5.")
        else:
            print(number, "is not divisible by 5.")
        
        if divisible_by_7:
            print(number, "is divisible by 7.")
        else:
            print(number, "is not divisible by 7.")
        
        if divisible_by_11:
            print(number, "is divisible by 11.")
        else:
            print(number, "is not divisible by 11.")
        
        if is_even:
            print(number, "is even.")
        else:
            print(number, "is odd.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
