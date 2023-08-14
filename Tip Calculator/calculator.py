# Function that calculates the tip amount and total amount of a bill
def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100) # Tip amount is calculated by multiplying the bill amount by the tip percentage
    total_amount = bill_amount + tip_amount # Total amount is calculated by adding the bill amount and tip amount
    return tip_amount, total_amount # Returns the tip amount and total amount

def main():
    try:
        bill_amount = float(input("Enter the bill amount: $"))
        tip_percentage = [10, 15, 20, 25, 30]

        print("Select tip percentage:")
        for idx, percentage in enumerate(tip_percentage, start=1): # Enumerates the tip percentage list and prints the index and percentage
            print(f"{idx}. {percentage}%") # Prints the index and percentage

        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > len(tip_percentage):
            print("Invalid choice. Please try again.")

        else:
            tip_percentage = tip_percentage[choice - 1] # Tip percentage is set to the index of the choice minus 1
            tip_amount, total_amount = calculate_tip(bill_amount, tip_percentage) # Tip amount and total amount are set to the return values of the calculate_tip function
            print(f"Bill Amount: ${bill_amount:.2f}") # Prints the bill amount with 2 decimal places
            print(f"Tip Amount ({tip_percentage}%): ${tip_amount:.2f}") # Prints the tip amount with 2 decimal places
            print(f"Total Amount: ${total_amount:.2f}") # Prints the total amount with 2 decimal places

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__": # Runs the main function
    main() # Calls the main function
