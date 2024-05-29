def calculate_gross_pay(hours_worked, rate_per_hour):
    return hours_worked * rate_per_hour

def main():
    try:
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter rate per hour: "))
        
        if hours < 0 or rate < 0:
            print("Hours and rate must be positive numbers.")
        else:
            gross_pay = calculate_gross_pay(hours, rate)
            print("Gross pay: $", format(gross_pay, ".2f"))
    except ValueError:
        print("Please enter valid numbers for hours worked and rate per hour.")

if __name__ == "__main__":
    main()
